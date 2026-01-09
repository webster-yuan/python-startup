from fastapi import HTTPException
from fastapi import APIRouter, Depends, Cookie, Header
from typing import Annotated

depends_router = APIRouter(prefix="/depends_router", tags=["depends_router"])


# 依赖项必需是可调用对象
# 1. 函数
async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}


@depends_router.get("/items")
async def get_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons


# 2. 类
class CommonParameter:
    q: str
    skip: int
    limit: int

    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@depends_router.post("/items")
async def post_items(commons: Annotated[CommonParameter, Depends(CommonParameter)]):
    """
    FastAPI会调用该类CommonQueryParams。
    这将创建一个该类的“实例”，并将该实例作为参数传递commons给您的函数。
    第一个CommonQueryParams,对FastAPI来说没有任何特殊意义。
    FastAPI 不会使用它进行数据转换、验证等操作（因为它使用 来进行Depends(CommonQueryParams)这些操作）。
    但建议声明类型，这样编辑器就能知道参数是什么commons，从而帮助你进行代码补全、类型检查等等
    强迫症不写重复代码的话，可以换成
    commons: Annotated[CommonParameter, Depends()]
    FastAPI也知道怎么做
    """
    response = {}
    if commons.q:
        response.update({"q": commons.q})

    items = fake_items_db[commons.skip:commons.skip + commons.limit]
    response.update({"items": items})
    return response


# 子依赖项

def query_extractor(q: str | None = None):
    return q


def query_or_cookie_extractor(
        q: Annotated[str, Depends(query_extractor)],
        last_query: Annotated[str | None, Cookie()] = None,
):
    if q is None:
        return last_query

    return q


@depends_router.get("/sub/dependencies/items")
async def sub_get_items(
        query_or_default: Annotated[str, Depends(query_or_cookie_extractor)]
):
    return {"query_or_default": query_or_default}


# 将依赖项（dependable）从路径操作函数参数中->放到路径操作装饰器
# 声明一个 dependencies 列表
async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=422, detail="X-Token header invalid")


async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")

    return x_key


@depends_router.get("/verify/items", dependencies=[Depends(verify_token), Depends(verify_key)])
async def verify_items():
    """
    这些依赖项将被执行/解决，方式与普通依赖项相同。但它们的值（如果它们返回任何值）不会传递给您的路径操作函数
    """
    return {"items": fake_items_db}


# 全局依赖项
# app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])

# yield 依赖项
data = {
    "plumbus": {"description": "Freshly pickled plumbus", "owner": "Morty"},
    "portal-gun": {"description": "Gun to create portals", "owner": "Rick"},
}


class OwnerError(Exception):
    pass


class InternalError(Exception):
    pass


def get_username():
    try:
        yield "Rick"
    except InternalError:
        print("We don't swallow the internal error here, we raise again 😎")
        raise  # 这里需要把异常抛出去
    except OwnerError as e:
        raise HTTPException(status_code=400, detail=f"Owner error: {e}")


@depends_router.get("/items/{item_id}")
def get_item(item_id: str, username: Annotated[str, Depends(get_username)]):
    if item_id not in data:
        raise HTTPException(status_code=404, detail="Item not found")
    item = data[item_id]
    if item["owner"] != username:
        raise OwnerError(username)
    return item


# 提前退出和 scope
# 通常，带有 yield 的依赖项的退出代码会在响应发送给客户端 **之后** 执行。
# 但是，如果您知道在从 *路径操作函数* 返回后不再需要使用该依赖项，
# 您可以使用 Depends(scope="function") 来告诉 FastAPI 它应该在
# *路径操作函数* 返回后、**但在响应发送之前** 关闭该依赖项。
def get_username():
    try:
        yield "Rick"
    finally:
        print("Cleanup up before response is sent")


@depends_router.get("/users/me")
def get_user_me(username: Annotated[str, Depends(get_username, scope="function")]):
    """
    Depends() 接收一个 scope 参数，它可以是
    1. "function"：在处理请求的 *路径操作函数* 之前启动依赖项，
        在 *路径操作函数* 结束之后、**但在响应发送回客户端之前** 结束依赖项。因此，依赖项函数将在 *路径操作* **函数** *的周围* 执行。
    2. "request"：在处理请求的 *路径操作函数* 之前启动依赖项（与使用 "function" 时类似），
        但在响应发送回客户端 **之后** 结束。因此，依赖项函数将在 **请求** 和响应周期 *的周围* 执行。
        如果未指定并且依赖项带有 yield，则默认情况下其 scope 为 "request"。

    ps：
    当您声明一个带有 scope="request"（默认值）的依赖项时，任何子依赖项也必须具有 scope 为 "request"
    但是，一个带有 scope 为 "function" 的依赖项可以有 scope 为 "function" 和 scope 为 "request" 的子依赖项。
    这是因为任何依赖项都需要能够在子依赖项之前执行其退出代码，
    因为它可能需要在其退出代码中仍使用它们。
    """
    return username


# context manager with dependencies

class MySuperContextManager:
    def __init__(self):
        self.db = "fake db"

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, exc_trace_back):
        self.db = ""  # 实际应该是Close()


async def get_fake_db():
    with MySuperContextManager() as db:
        yield db
