---

## 一、为什么 `APIRouter` 不能直接用 `exception_handler`

### 官方设计层面

FastAPI 的异常处理是基于 **Starlette 的 ExceptionMiddleware**，而这个中间件：

* **只存在于 ASGI App（FastAPI 实例）级别**
* `APIRouter` 只是：

    * 路由收集器
    * 不是真正的 ASGI 应用

所以：

```python
@exception_router.exception_handler()
```

❌ **这是不支持的**（即使你看到 IDE 不报错，运行时也不会生效）

官方只支持：

```python
@app.exception_handler(ExceptionType)
```

---

## 二、推荐的标准做法（你现在这个阶段最合适的）

### ✅ 方案 1：集中在 `exception.py`，在 `main.py` 全局注册（推荐）

这是 **FastAPI 官方 & 企业项目最常见结构**。

### 1️⃣ exception.py

```python
from fastapi import Request
from fastapi.responses import JSONResponse


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


async def unicorn_exception_handler(
        request: Request,
        exc: UnicornException
):
    return JSONResponse(
        status_code=418,
        content={
            "error": "UnicornException",
            "name": exc.name,
            "path": request.url.path
        }
    )
```

---

### 2️⃣ main.py

```python
from fastapi import FastAPI
from exception import UnicornException, unicorn_exception_handler
from routers import exception_router

app = FastAPI()

# ✅ 全局注册
app.add_exception_handler(
    UnicornException,
    unicorn_exception_handler
)

app.include_router(exception_router)
```

---

### 3️⃣ router 中直接抛异常即可

```python
from fastapi import APIRouter
from exception import UnicornException

exception_router = APIRouter()


@exception_router.get("/test")
async def test_exception():
    raise UnicornException("Rainbow Dash")
```

✅ **不管异常从哪个 router 抛出，都会被捕获**

---

## 三、如果你“真的”想局部生效，有 2 种高级方案

### 🚀 方案 2：使用「子应用（Sub-App）」——真正的“局部异常处理”

这是 FastAPI **唯一支持的局部异常方案**。

```python
sub_app = FastAPI()


@sub_app.exception_handler(UnicornException)
async def handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"msg": f"sub app error: {exc.name}"}
    )


router = APIRouter()


@router.get("/boom")
async def boom():
    raise UnicornException("sub")


sub_app.include_router(router)

app.mount("/api/v2", sub_app)
```

访问：

```
/api/v2/boom
```

✔️ 只在 `/api/v2` 下生效

📌 **适合：多版本 API / 微服务风格**

---

### 🧱 方案 3：中间件（适合统一日志 / 包装异常）

```python
@app.middleware("http")
async def exception_middleware(request, call_next):
    try:
        return await call_next(request)
    except UnicornException as e:
        return JSONResponse(
            status_code=400,
            content={"msg": e.name}
        )
```

📌 **适合：**

* 日志
* 统一错误格式
* 不关心异常类型太多

---

## 四、为什么不建议“router 级异常处理”（面试点）

你可以这样说 👇

> FastAPI 的异常处理是通过 ASGI 应用层的 ExceptionMiddleware 实现的，而 APIRouter 只是路由的组织结构，不具备独立的异常处理能力。因此官方只支持在
> FastAPI 应用实例上注册异常处理器。如果需要局部异常处理，通常通过子应用（mount FastAPI）或者中间件来实现。

💯 **这是面试官想听的答案**

---

## 五、总结（直接记住这张表）

| 需求               | 正确方式                        |
|------------------|-----------------------------|
| 全局异常             | `app.add_exception_handler` |
| router 抛异常       | ✅ 直接 `raise`                |
| router 级 handler | ❌ 不支持                       |
| 局部异常             | 子应用（FastAPI + mount）        |
| 日志/统一格式          | Middleware                  |

---

如果你愿意，我可以帮你：

* 设计一套 **企业级异常基类（ErrorCode / ErrorResponse）**
* 或把异常体系和 **前端 error code** 对齐
* 或模拟一个 **面试标准答案 + 追问**

你现在问的这个问题，已经是 **中高级 FastAPI 使用者** 才会踩到的坑了 👍
