# webster_api/main.py
import time
from contextlib import asynccontextmanager
from urllib.request import Request

from fastapi import FastAPI
import logging
import uvicorn
from routers import path_param_router, query_param_router, req_body_router, other_data_type_router, \
    header_cookie_router, header_router, exception_router, depends_router

from exception import UnicornException, unicorn_exception_handler

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

app.add_exception_handler(UnicornException, unicorn_exception_handler)


# openapi中每个HTTP方法都被称为操作
@app.get("/")  # 路径操作装饰器：告诉FastAPI，下面的函数负责处理发送到=> 路径：/ 使用 get 操作
def read_root():
    return "hello webster"


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.include_router(path_param_router)
app.include_router(query_param_router)
app.include_router(req_body_router)
app.include_router(other_data_type_router)
app.include_router(header_cookie_router)
app.include_router(header_router)
app.include_router(exception_router)
app.include_router(depends_router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
