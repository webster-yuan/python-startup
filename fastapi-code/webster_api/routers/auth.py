"""
认证路由
包含登录、注册、刷新 Token 等功能
"""
from typing import Annotated
from fastapi import APIRouter, Depends, status, Body, Response, Request, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from webster_api.db.sqlite import SessionDep
from webster_api.core.deps import get_current_active_user
from webster_api.core.rate_limit import rate_limiter
from webster_api.core.ip import get_client_ip
from webster_api.models.user import User
from webster_api.schemas.user import UserCreate, UserRead, Token
from webster_api.config import settings
from webster_api.services.user import (
    create_user_service,
    login_service,
    refresh_token_service,
    logout_service,
    get_current_user_service
)

auth_router = APIRouter(prefix="/auth", tags=["authentication"])


@auth_router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def register(
    user_create: UserCreate,
    session: SessionDep
):
    """
    用户注册
    
    - **username**: 用户名（3-50个字符）
    - **email**: 邮箱地址
    - **password**: 密码（至少6个字符）
    """
    return create_user_service(session, user_create)


@auth_router.post("/login", response_model=Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: SessionDep,
    request: Request,
):
    """
    用户登录
    
    使用 OAuth2 标准的表单格式：
    - **username**: 用户名
    - **password**: 密码
    
    返回 JWT access token，用于后续 API 认证
    
    注意：业务逻辑在 Service 层，这里只负责调用 Service 和返回响应。
    如果认证失败，Service 层会抛出 AuthenticationError 业务异常，
    由全局异常处理器统一转换为 HTTP 401 响应。
    """
    client_ip = get_client_ip(
        request,
        trust_proxy_headers=settings.trust_proxy_headers,
        trusted_proxies=settings.trusted_proxies,
    )
    key = f"auth:login:{client_ip}:{form_data.username}"
    if not rate_limiter.allow(key, limit=10, window_seconds=60):
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="Too many login attempts")

    ua = request.headers.get("user-agent")
    return login_service(session, form_data.username, form_data.password, client_ip=client_ip, user_agent=ua)


@auth_router.post("/refresh", response_model=Token)
async def refresh_token(
    refresh_token: Annotated[str, Body(embed=True, description="Refresh token")],
    session: SessionDep,
    request: Request,
):
    """
    刷新 Access Token
    
    使用 Refresh Token 获取新的 Access Token。
    - **refresh_token**: Refresh Token 字符串
    
    返回新的 Access Token，并**轮换** Refresh Token（Refresh Rotation）。
    客户端必须使用响应中的新 refresh_token 替换旧的，否则旧 token 会立即失效。
    
    注意：业务逻辑在 Service 层，这里只负责调用 Service 和返回响应。
    如果 Refresh Token 无效/已过期/已被轮换，Service 层会抛出 RefreshTokenError 业务异常，
    由全局异常处理器统一转换为 HTTP 401 响应。
    """
    client_ip = get_client_ip(
        request,
        trust_proxy_headers=settings.trust_proxy_headers,
        trusted_proxies=settings.trusted_proxies,
    )
    key = f"auth:refresh:{client_ip}"
    if not rate_limiter.allow(key, limit=30, window_seconds=60):
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="Too many refresh attempts")

    ua = request.headers.get("user-agent")
    return refresh_token_service(session, refresh_token, client_ip=client_ip, user_agent=ua)


@auth_router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(
    refresh_token: Annotated[str, Body(embed=True, description="Refresh token")],
    session: SessionDep,
    request: Request,
) -> Response:
    """
    Logout（注销）

    - 客户端提供当前的 refresh_token（opaque token）
    - 服务端撤销对应的会话（refresh session）
    - 该接口是幂等的：token 不存在/已撤销也会返回 204
    """
    client_ip = get_client_ip(
        request,
        trust_proxy_headers=settings.trust_proxy_headers,
        trusted_proxies=settings.trusted_proxies,
    )
    key = f"auth:logout:{client_ip}"
    if not rate_limiter.allow(key, limit=60, window_seconds=60):
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="Too many logout attempts")

    logout_service(session, refresh_token)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@auth_router.get("/me", response_model=UserRead)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """
    获取当前登录用户信息
    
    需要 Bearer Token 认证
    """
    return get_current_user_service(current_user)
