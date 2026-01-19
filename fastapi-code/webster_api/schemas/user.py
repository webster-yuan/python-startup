"""
用户相关的 Schema
"""
from pydantic import BaseModel, EmailStr, ConfigDict, Field

from webster_api.core.constants import BEARER_TOKEN_TYPE, BCRYPT_MAX_PASSWORD_BYTES


class UserBase(BaseModel):
    """用户基础 Schema"""
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr


class UserCreate(UserBase):
    """创建用户 Schema"""
    password: str = Field(
        ...,
        min_length=6,
        max_length=BCRYPT_MAX_PASSWORD_BYTES,  # bcrypt 限制：密码不能超过 BCRYPT_MAX_PASSWORD_BYTES 字节
        description=f"密码长度必须在 6-{BCRYPT_MAX_PASSWORD_BYTES} 个字符之间"
    )


class UserLogin(BaseModel):
    """用户登录 Schema"""
    username: str
    password: str


class Token(BaseModel):
    """Token 响应 Schema"""
    access_token: str
    refresh_token: str | None = None
    token_type: str = BEARER_TOKEN_TYPE


class TokenData(BaseModel):
    """Token 数据 Schema"""
    username: str | None = None


class ORMBase(BaseModel):
    """ORM 基础 Schema"""
    model_config = ConfigDict(from_attributes=True)


class UserRead(ORMBase):
    """用户读取 Schema"""
    id: int
    username: str
    email: str
    is_active: bool
    is_superuser: bool
