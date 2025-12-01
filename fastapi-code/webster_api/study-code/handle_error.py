from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import PlainTextResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

items = {"foo": "the foo wrestlers"}

# 1. 抛异常
# HTTPException是一个Python异常,不会return ,而是raise
# fastapi中的HTTPException detail中的内容可以是dict list等,fastapi会自动转为json格式返回
# 在路径操作函数中,调用实用程序函数,并在实用程序函数内部引发了HTTPException,将不会
# 运行路径操作函数后续代码,将立即终止该请求并将HTTP错误发送到客户端


@app.get("/items/{item_id}")
async def read_items(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}


# 2. 添加自定义头部
@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="item not found",
            headers={"X-Error": "There goes my error"},
        )
    return {"item": items[item_id]}


# 3. 安装自定义异常处理程序 或者 使用 Starlette 中相同的异常实用程序 添加自定义异常处理程序
# 3.1 自定义异常,并且交给fastapi全局处理异常
class UnicornException(Exception):
    def __init__(self, name: str) -> None:
        self.name = name


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )


# 3.2 使用 Starlette 中相同的异常实用程序 添加自定义异常处理程序
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}


# 4. 覆盖fastapi默认处理程序,使用装饰器
# 4.1. 覆盖请求验证异常
# 请求无效数据时,FastAPI会在内部引发RequestValidationError,
# 并且它还包含一个默认的异常处理程序,用如下方式实现覆盖:
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.get("/items/{item_id}")
async def read_items(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}


# RequestValidationError 是Pydantic的ValidationError子类,
# 如果数据存在错误,会在日志中看到,客户端收到500


# 4.2 覆盖HTTPException错误处理程序
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request:Request, exc:StarletteHTTPException):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}


# 使用RequestValidationError主体
# 包含它接收到的 包含无效数据的body


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


class Item(BaseModel):
    title: str
    size: int


@app.post("/items/")
async def create_item(item: Item):
    return item

# FastAPI的HTTPException错误类继承自Starlette的HTTPException错误类。
# 唯一的区别是FastAPI的HTTPException接受任何可JSON化的数据作为detail字段，
# 而Starlette的HTTPException仅接受字符串
# 当您注册异常处理程序时，应将其注册为Starlette的HTTPException