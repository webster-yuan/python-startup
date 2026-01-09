from fastapi import Depends
from sqlalchemy import create_engine
from typing import Annotated
from sqlmodel import SQLModel, Session

sqlite_file_name = "db/database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}  # 允许 FastAPI 在不同线程中使用同一个 SQLite 数据库
# create_engine 创建所有表模型的表
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
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
