# webster_api/main.py
import time
from contextlib import asynccontextmanager
from urllib.request import Request

from fastapi import FastAPI
import logging
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from exception import BusinessException, InfraException, SystemException
from webster_api.config import settings
from webster_api.db.sqlite import create_db_and_tables
from webster_api.routers import test_router, api_router

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(web: FastAPI):
    logger.info(f"Webster-Api starting!")
    # 可以在这里初始化数据库、连接池等
    create_db_and_tables()

    # 打印注册的路由
    for route in web.routes:
        print(f"Path:{getattr(route, 'path', None)}, method:{getattr(route, 'method', None)}")

    yield

    logger.info(f"Webster-Api shut down !")


app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    lifespan=lifespan
)  # app是FastAPI类的实例，创建API的主要交互点


@app.exception_handler(BusinessException)
@app.exception_handler(SystemException)
@app.exception_handler(InfraException)
def error_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )


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


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,  # 允许访问的来源列表
    allow_credentials=settings.cors_allow_credentials,  # 是否允许携带 Cookie
    allow_methods=settings.cors_allow_methods_list,  # 允许的 HTTP 方法
    allow_headers=settings.cors_allow_headers_list,  # 允许的请求头
)

app.include_router(test_router)
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.reload or settings.debug
    )
