"""
依赖注入模块
提供认证相关的依赖注入函数
"""
import logging
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import select

from webster_api.db.sqlite import SessionDep
from webster_api.models.user import User
from webster_api.core.security import decode_access_token
from webster_api.core.constants import (
    TOKEN_TYPE_ACCESS,
    JWT_CLAIM_SUB,
    JWT_CLAIM_TYPE,
    WWW_AUTHENTICATE_HEADER,
    BEARER_AUTH_SCHEME
)

logger = logging.getLogger(__name__)

# OAuth2 Password Bearer (OpenAPI + consistent 401)
# NOTE: Even if we include refresh_token in /auth/login response, the tokenUrl is still correct for the access token.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: SessionDep
) -> User:
    """
    获取当前认证用户
    
    从 Authorization header 中提取 token，验证并返回用户对象
    
    Raises:
        HTTPException: 如果 token 无效或用户不存在
    """
    token_data = decode_access_token(token)
    
    if token_data is None:
        logger.warning("Invalid token: failed to decode token")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={WWW_AUTHENTICATE_HEADER: BEARER_AUTH_SCHEME},
        )
    
    # 验证 token 类型（必须是 access token）
    token_type = token_data.get(JWT_CLAIM_TYPE)
    if token_type != TOKEN_TYPE_ACCESS:
        logger.warning(f"Invalid token type: expected '{TOKEN_TYPE_ACCESS}', got '{token_type}'")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={WWW_AUTHENTICATE_HEADER: BEARER_AUTH_SCHEME},
        )
    
    sub: str | int | None = token_data.get(JWT_CLAIM_SUB)
    if sub is None:
        logger.warning(f"Invalid token: missing '{JWT_CLAIM_SUB}' claim")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={WWW_AUTHENTICATE_HEADER: BEARER_AUTH_SCHEME},
        )

    try:
        user_id = int(sub)
    except (TypeError, ValueError):
        logger.warning(f"Invalid token: '{JWT_CLAIM_SUB}' is not a valid user id")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={WWW_AUTHENTICATE_HEADER: BEARER_AUTH_SCHEME},
        )
    
    # 从数据库查询用户
    statement = select(User).where(User.id == user_id)
    user = session.exec(statement).first()
    
    if user is None:
        logger.warning(f"User not found: user_id={user_id}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={WWW_AUTHENTICATE_HEADER: BEARER_AUTH_SCHEME},
        )
    
    if not user.is_active:
        logger.warning(f"Inactive user attempted access: user_id={user_id}")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user"
        )
    
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
) -> User:
    """
    获取当前激活的用户
    
    注意：get_current_user 已经验证了用户是否激活，
    此函数主要用于语义清晰和未来可能的扩展。
    """
    # get_current_user 已经验证了 is_active，这里不需要重复检查
    return current_user


# 注意：不能在这里直接使用 Depends(get_current_active_user) 作为类型别名
# 因为 FastAPI 的依赖注入需要在路由函数参数中明确声明
