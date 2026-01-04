# webster_api/main.py
from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn
from routers import path_param_router, query_param_router, req_body_router
import logging

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(web: FastAPI):
    logger.info(f"Webster-Api starting!")
    # 可以在这里初始化数据库、连接池等
    # 打印注册的路由
    for route in web.routes:
        print(f"Path:{getattr(route, 'path', None)}, method:{getattr(route, 'method', None)}")
    yield
    logger.info(f"Webster-Api shut down !")


app = FastAPI(lifespan=lifespan)  # app是FastAPI类的实例，创建API的主要交互点


# openapi中每个HTTP方法都被称为操作
@app.get("/")  # 路径操作装饰器：告诉FastAPI，下面的函数负责处理发送到=> 路径：/ 使用 get 操作
def read_root():
    return "hello webster"


app.include_router(path_param_router)
app.include_router(query_param_router)
app.include_router(req_body_router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
