"""
用户 CRUD 操作
"""
from typing import Sequence
from sqlmodel import Session, select

from webster_api.models.user import User


def get_user_by_username(session: Session, username: str) -> User | None:
    """根据用户名查询用户"""
    statement = select(User).where(User.username == username)
    return session.exec(statement).first()


def get_user_by_email(session: Session, email: str) -> User | None:
    """根据邮箱查询用户"""
    statement = select(User).where(User.email == email)
    return session.exec(statement).first()


def get_user_by_id(session: Session, user_id: int) -> User | None:
    """根据 ID 查询用户"""
    statement = select(User).where(User.id == user_id)
    return session.exec(statement).first()


def create_user(session: Session, username: str, email: str, hashed_password: str) -> User:
    """
    创建用户
    
    注意：CRUD 层接收哈希后的密码，不负责密码哈希
    密码哈希应该在 Service 层完成
    
    Args:
        session: 数据库会话
        username: 用户名
        email: 邮箱
        hashed_password: 哈希后的密码（不是明文）
    
    Returns:
        创建的 User Model
    """
    db_user = User(
        username=username,
        email=email,
        hashed_password=hashed_password
    )
    session.add(db_user)
    session.flush()
    return db_user


def get_users(session: Session, offset: int = 0, limit: int = 100) -> Sequence[User]:
    """获取用户列表"""
    statement = select(User).offset(offset).limit(limit)
    return session.exec(statement).all()
