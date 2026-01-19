"""
安全相关功能模块
包含密码加密、JWT token 生成和验证
"""
from datetime import datetime, timedelta, timezone
from typing import Any
from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError
from passlib.context import CryptContext

from webster_api.config import settings
from webster_api.core.constants import (
    JWT_CLAIM_EXP,
    JWT_CLAIM_ISS,
    JWT_CLAIM_AUD,
    BCRYPT_MAX_PASSWORD_BYTES,
)

# 密码加密上下文
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """验证密码"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    获取密码哈希值
    
    注意：bcrypt 限制的是明文密码的字节数（BCRYPT_MAX_PASSWORD_BYTES 字节），不是哈希后的密码长度。
    哈希后的密码长度通常是 60 个字符（固定长度）。
    
    Args:
        password: 明文密码（必须 ≤ BCRYPT_MAX_PASSWORD_BYTES 字节）
    
    Returns:
        加密后的密码哈希值（固定 60 字符）
    
    Raises:
        ValueError: 如果明文密码超过 BCRYPT_MAX_PASSWORD_BYTES 字节（bcrypt 限制）
        AttributeError: 如果 bcrypt 版本不兼容
    """
    # bcrypt 限制：明文密码不能超过 BCRYPT_MAX_PASSWORD_BYTES 字节
    # 这个检查作为最后一道防线（Service 层应该已经检查过）
    password_bytes = password.encode('utf-8')
    if len(password_bytes) > BCRYPT_MAX_PASSWORD_BYTES:
        raise ValueError(
            f"Password is too long. Maximum length is {BCRYPT_MAX_PASSWORD_BYTES} bytes (plain text). "
            f"Your password is {len(password_bytes)} bytes. "
            f"Please use a shorter password."
        )
    
    # 对明文密码进行 bcrypt 哈希（哈希后长度固定为 60 字符）
    try:
        return pwd_context.hash(password)
    except AttributeError:
        # bcrypt 版本兼容性错误（AttributeError 通常表示 bcrypt/passlib 版本不兼容）
        # 重新抛出一个更明确的错误信息，但保持异常类型不变
        # 注意：这里不再匹配错误消息字符串，直接假设所有 AttributeError 都是兼容性问题
        # 如果未来有其他 AttributeError，这里可能需要更细粒度的判断
        raise AttributeError(
            "bcrypt version compatibility error. "
            "Please ensure bcrypt version is compatible with passlib. "
            "Try: pip install 'bcrypt>=3.1.0,<5.0.0'"
        )


def create_access_token(data: dict[str, Any], expires_delta: timedelta | None = None) -> str:
    """
    创建 JWT access token
    
    Args:
        data: 要编码到 token 中的数据（通常是 username 或 user_id）
        expires_delta: 过期时间增量，如果为 None 则使用配置中的默认值
    
    Returns:
        JWT token 字符串
    """
    to_encode = data.copy()
    
    now = datetime.now(timezone.utc)
    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now + timedelta(minutes=settings.access_token_expire_minutes)
    
    # 添加 JWT 标准字段（企业基线：iss/aud）
    to_encode.update({
        JWT_CLAIM_ISS: settings.jwt_issuer,
        JWT_CLAIM_AUD: settings.jwt_audience,
        JWT_CLAIM_EXP: expire,
        "iat": now  # Issued At - JWT 标准字段，记录 token 发行时间
    })
    encoded_jwt = jwt.encode(
        to_encode,
        settings.secret_key,
        algorithm=settings.algorithm,
        headers={"kid": settings.jwt_signing_kid},
    )
    return encoded_jwt


def decode_access_token(token: str) -> dict[str, Any] | None:
    """
    解码 JWT access token
    
    Args:
        token: JWT token 字符串
    
    Returns:
        解码后的 token 数据，如果 token 无效或已过期则返回 None
    
    Note:
        jwt.decode() 会自动验证 token 的签名、过期时间（exp）等
        过期时会抛出 ExpiredSignatureError，格式错误会抛出其他 JWTError
    """
    try:
        header = jwt.get_unverified_header(token)
        kid = header.get("kid")
    except JWTError:
        kid = None

    # Try selected key first (by kid), then fallback to all known keys.
    keyring = settings.jwt_keyring
    keys_to_try: list[str] = []
    if isinstance(kid, str) and kid in keyring:
        keys_to_try.append(keyring[kid])
    # Keep deterministic order for remaining keys
    for _, k in sorted(keyring.items()):
        if k not in keys_to_try:
            keys_to_try.append(k)

    for key in keys_to_try:
        try:
            payload = jwt.decode(
                token,
                key,
                algorithms=[settings.algorithm],
                issuer=settings.jwt_issuer,
                audience=settings.jwt_audience,
            )
            return payload
        except ExpiredSignatureError:
            return None
        except JWTError:
            continue

    return None
