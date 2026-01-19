"""
用户服务层
"""
import logging
import hashlib
import secrets
from datetime import timedelta, datetime, timezone
from sqlmodel import Session

from webster_api.models.user import User
from webster_api.schemas.user import UserCreate, UserRead, Token
from webster_api.crud.user import (
    get_user_by_username,
    get_user_by_email,
    create_user as crud_create_user,
    get_user_by_id,
)
from webster_api.crud.auth_session import (
    create_auth_session,
    get_active_session_by_refresh_hash,
    get_session_by_refresh_hash,
    revoke_session,
    touch_session_last_used,
)
from webster_api.exception.base import BusinessException
from webster_api.core.security import (
    create_access_token,
    verify_password,
    get_password_hash
)
from webster_api.core.constants import (
    TOKEN_TYPE_ACCESS,
    JWT_CLAIM_SUB,
    JWT_CLAIM_TYPE,
    BEARER_TOKEN_TYPE,
    BCRYPT_MAX_PASSWORD_BYTES
)
from webster_api.config import settings

logger = logging.getLogger(__name__)

def _new_refresh_token() -> str:
    # Opaque token (do not store plaintext in DB)
    return secrets.token_urlsafe(48)


def _hash_refresh_token(refresh_token: str) -> str:
    return hashlib.sha256(refresh_token.encode("utf-8")).hexdigest()


class UserExistsError(BusinessException):
    """用户已存在异常"""
    # 语义：资源冲突（用户名/邮箱已被占用）
    status_code = 409
    detail = "User already exists"


class AuthenticationError(BusinessException):
    """认证失败异常"""
    status_code = 401
    detail = "Incorrect username or password"


class PasswordValidationError(BusinessException):
    """密码验证失败异常"""
    status_code = 400
    detail = "Password validation failed"


def create_user_service(session: Session, user_create: UserCreate) -> UserRead:
    """
    创建用户服务
    
    Args:
        session: 数据库会话
        user_create: 用户创建 Schema
    
    Returns:
        创建的用户信息
    
    Raises:
        UserExistsError: 如果用户名或邮箱已存在
        PasswordValidationError: 如果密码不符合要求（如超过72字符）
    """
    # 检查用户名是否已存在
    if get_user_by_username(session, user_create.username):
        raise UserExistsError("Username already registered")

    # 检查邮箱是否已存在
    if get_user_by_email(session, str(user_create.email)):
        raise UserExistsError("Email already registered")

    # 验证密码长度（bcrypt 限制：明文密码不能超过 BCRYPT_MAX_PASSWORD_BYTES 字节）
    # 注意：bcrypt 限制的是明文密码的字节数，不是哈希后的密码
    # 对于纯 ASCII 字符，1字符=1字节
    # 对于包含中文等 Unicode 字符的情况，实际字节数可能超过字符数
    # 例如：一个中文字符 "中" 占 3 个字节（UTF-8）
    # Schema 层已经限制了字符数（max_length=BCRYPT_MAX_PASSWORD_BYTES），这里检查字节数作为额外保障
    password_bytes = user_create.password.encode('utf-8')
    if len(password_bytes) > BCRYPT_MAX_PASSWORD_BYTES:
        raise PasswordValidationError(
            f"Password is too long. Maximum length is {BCRYPT_MAX_PASSWORD_BYTES} bytes. "
            f"Your password is {len(password_bytes)} bytes. "
            f"Please use a shorter password."
        )

    # 创建用户
    # Service 层职责：Schema → Model 转换，密码哈希
    # 注意：密码哈希应该在 Service 层完成，而不是 CRUD 层
    try:
        # 密码哈希（Service 层职责）
        hashed_password = get_password_hash(user_create.password)
    except ValueError as e:
        # ValueError: 密码长度超过限制（由 security.py 中的检查抛出）
        # security.py 已经提供了明确的错误消息，直接转换为业务异常
        logger.warning(f"Password validation failed: password too long - {str(e)}")
        raise PasswordValidationError(
            f"Password is too long. Maximum length is {BCRYPT_MAX_PASSWORD_BYTES} bytes. "
            "Please use a shorter password."
        )
    except AttributeError as e:
        # AttributeError: bcrypt 版本兼容性问题（由 security.py 转换后抛出）
        # security.py 已经提供了明确的错误消息，转换为业务异常
        logger.error(f"Password encryption error: bcrypt compatibility issue - {str(e)}")
        raise PasswordValidationError(
            "Password encryption service is temporarily unavailable. "
            "Please contact the administrator or try again later."
        )
    
    # EmailStr 类型需要转换为 str 传递给 CRUD 层
    # CRUD 层接收哈希后的密码
    db_user = crud_create_user(
        session,
        username=user_create.username,
        email=str(user_create.email),  # 将 EmailStr 转换为 str
        hashed_password=hashed_password  # 传递哈希后的密码
    )

    logger.info(f"User created successfully: username={db_user.username}, user_id={db_user.id}, email={db_user.email}")

    # Service 层职责：Model → Schema 转换
    return UserRead.model_validate(db_user)


def authenticate_user(session: Session, username: str, password: str) -> User | None:
    """
    验证用户（内部函数，由服务层调用）
    
    Args:
        session: 数据库会话
        username: 用户名
        password: 密码（明文）
    
    Returns:
        用户对象，如果认证失败返回 None
    """
    user = get_user_by_username(session, username)
    if not user:
        logger.warning(f"Authentication failed: user not found (username={username})")
        return None

    # 验证明文密码与哈希密码是否匹配
    if not verify_password(password, user.hashed_password):
        logger.warning(f"Authentication failed: incorrect password (username={username})")
        return None

    logger.info(f"Authentication successful: username={username}, user_id={user.id}")
    return user


def login_service(
    session: Session,
    username: str,
    password: str,
    *,
    client_ip: str | None = None,
    user_agent: str | None = None,
) -> Token:
    """
    登录服务
    
    Args:
        session: 数据库会话
        username: 用户名
        password: 密码（明文）
    
    Returns:
        Token 对象（包含 access_token 和 refresh_token）
    
    Raises:
        AuthenticationError: 如果认证失败
    """
    user = authenticate_user(session, username, password)
    if not user:
        raise AuthenticationError()

    # 创建 access token
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        # Use immutable subject (user_id) instead of username
        data={JWT_CLAIM_SUB: str(user.id), JWT_CLAIM_TYPE: TOKEN_TYPE_ACCESS},
        expires_delta=access_token_expires
    )

    # Create opaque refresh token session (store hash only)
    refresh_token = _new_refresh_token()
    refresh_hash = _hash_refresh_token(refresh_token)
    refresh_expires_at = datetime.now(timezone.utc) + timedelta(days=settings.refresh_token_expire_days)
    create_auth_session(
        session,
        user_id=user.id,
        refresh_token_hash=refresh_hash,
        expires_at=refresh_expires_at,
        created_ip=client_ip,
        user_agent=user_agent,
    )

    return Token(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type=BEARER_TOKEN_TYPE
    )


class RefreshTokenError(BusinessException):
    """Refresh Token 无效异常"""
    status_code = 401
    detail = "Invalid refresh token"


def logout_service(session: Session, refresh_token: str) -> None:
    """
    Logout: revoke refresh token session.

    Security note:
    - Do not leak whether token existed; caller can treat invalid token as logged out.
    """
    refresh_hash = _hash_refresh_token(refresh_token)
    auth_session = get_session_by_refresh_hash(session, refresh_hash)
    if not auth_session:
        # Idempotent: treat as already logged out
        return
    revoke_session(session, auth_session)


def refresh_token_service(
    session: Session,
    refresh_token: str,
    *,
    client_ip: str | None = None,
    user_agent: str | None = None,
) -> Token:
    """
    刷新 Access Token 服务
    
    Args:
        session: 数据库会话
        refresh_token: Refresh Token 字符串
    
    Returns:
        Token 对象（包含新的 access_token）
    
    Raises:
        RefreshTokenError: 如果 refresh token 无效
    """
    # Enterprise baseline: refresh token is opaque; validate by hash lookup (rotation + revoke supported)
    refresh_hash = _hash_refresh_token(refresh_token)
    auth_session = get_active_session_by_refresh_hash(session, refresh_hash)
    if not auth_session:
        logger.warning("Refresh token failed: token not found / revoked / expired")
        raise RefreshTokenError("Invalid refresh token")

    user = get_user_by_id(session, auth_session.user_id)
    if not user:
        logger.warning(f"Refresh token failed: user not found (user_id={auth_session.user_id})")
        raise RefreshTokenError("Invalid refresh token")

    if not user.is_active:
        logger.warning(f"Refresh token failed: inactive user (username={user.username})")
        raise RefreshTokenError("User is not active")

    # Mark old session used + rotate refresh token (anti-replay)
    touch_session_last_used(session, auth_session)

    new_refresh_token = _new_refresh_token()
    new_refresh_hash = _hash_refresh_token(new_refresh_token)
    refresh_expires_at = datetime.now(timezone.utc) + timedelta(days=settings.refresh_token_expire_days)
    create_auth_session(
        session,
        user_id=user.id,
        refresh_token_hash=new_refresh_hash,
        expires_at=refresh_expires_at,
        created_ip=client_ip,
        user_agent=user_agent,
    )
    revoke_session(session, auth_session, replaced_by_hash=new_refresh_hash)

    # 创建新的 access token
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        # Use immutable subject (user_id) instead of username
        data={JWT_CLAIM_SUB: str(user.id), JWT_CLAIM_TYPE: TOKEN_TYPE_ACCESS},
        expires_delta=access_token_expires
    )

    logger.info(f"Access token refreshed successfully: username={user.username}, user_id={user.id}")

    # 返回新的 access token + rotated refresh token
    return Token(
        access_token=access_token,
        refresh_token=new_refresh_token,
        token_type=BEARER_TOKEN_TYPE
    )


def get_current_user_service(user: User) -> UserRead:
    """
    获取当前用户服务（Model → Schema 转换）
    
    Args:
        user: 用户 Model
    
    Returns:
        用户 Read Schema
    """
    # Service 层职责：Model → Schema 转换
    return UserRead.model_validate(user)
