from fastapi import Depends
from sqlalchemy import create_engine
from typing import Annotated
from sqlmodel import SQLModel, Session

from webster_api.config import settings

# 从配置读取数据库 URL
database_url = settings.database_url

# 如果是 SQLite，使用配置的连接参数
connect_args = {}
if database_url.startswith("sqlite"):
    connect_args = {"check_same_thread": settings.sqlite_check_same_thread}

# create_engine 创建所有表模型的表
engine = create_engine(database_url, connect_args=connect_args)


def create_db_and_tables():
    # Ensure all models are imported so SQLModel metadata is complete
    # (otherwise new tables like AuthSession may not be created).
    import webster_api.models  # noqa: F401
    SQLModel.metadata.create_all(engine)


def get_session():
    """
    service 层 不用写 commit / rollback
    事务自动管理
    异常自动回滚
    """
    session = Session(engine)
    try:
        yield session
        session.commit()  # 在这里commit，放弃在 service 层手动操作
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


SessionDep = Annotated[Session, Depends(get_session)]
