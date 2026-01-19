"""
用户模型
"""
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    """用户表模型"""
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    # 存储的是加密后的密码
    hashed_password: str
    # Refresh Token 已迁移到 AuthSession 表（仅存 hash + 元数据，支持 rotation / revoke）
    # 是否激活
    is_active: bool = Field(default=True)
    # 是否超级用户
    is_superuser: bool = Field(default=False)
