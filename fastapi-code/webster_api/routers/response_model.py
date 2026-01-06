from typing import Any, Union

from fastapi import APIRouter, Response, status
from pydantic import BaseModel, EmailStr
from fastapi.responses import RedirectResponse

response_router = APIRouter(prefix="/response", tags=["response"])

"""
返回类型声明为 Pydantic 模型

验证返回的数据
    如果数据无效（例如，您缺少一个字段），这意味着您的应用程序代码已损坏，
    未返回应有的内容，并且会返回服务器错误而不是错误的数据。
    这样，您和您的客户就可以确信他们将收到预期的数据和数据形状
为响应添加JSON Schema，在 OpenAPI 的路径操作中
    这将由自动文档使用。
    它也将被自动客户端代码生成工具使用
将限制和过滤输出数据，使其仅包含在返回类型中定义的内容
"""


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@response_router.post("/datatype_items/")
async def datatype_create_item(item: Item) -> Item:
    return item


@response_router.get("/items/")
async def datatype_read_items() -> list[Item]:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]


"""
路径操作装饰器参数 response_model
需要或希望返回的数据与声明的类型不完全匹配,
如果您添加了返回类型注解，工具和编辑器会报告一个（正确的）错误，
告诉您函数返回的类型（例如 dict）与您声明的类型（例如 Pydantic 模型）不同
"""


@response_router.post("/models/items/", response_model=Item)
async def models_create_item(item: Item) -> Any:
    """
    如果编辑器启动了严格类型检查，不声明返回类型会报错，
    可以有意告诉编辑器您有意返回任何内容。但是 FastAPI 仍然会使用 response_model 来进行数据文档、验证、过滤等工作
    """
    return item


@response_router.get("/items/", response_model=list[Item])
async def models_read_items() -> Any:
    """
    response_model 优先级大于 返回类型
    """
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]


# 返回类型和数据过滤
# 可以使用类和继承来利用函数类型注解，以获得更好的编辑器和工具支持，并仍然获得 FastAPI 的数据过滤
class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(BaseUser):
    password: str


@response_router.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user


@response_router.get("/portal", response_model=None)
async def get_portal(teleport: bool = False) -> Response | dict:
    """
    注解是一个联合模型，并且包含非 Pydantic 模型，Fastapi会先尝试从类型注解创建 Pydantic 相应模型导致失败，
    如果确实有这样的需求，那么可以设置 response_model=None 来禁用响应模型的生成，
    这样就可以有任何所需的返回类型注解
    """
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    return {"message": "Here's your interdimensional portal."}


# 响应模型默认值设置
class ResponseItem(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@response_router.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    """
    如果响应模型存在默认值，并且响应数据中没有这个字段的值，并且不希望返回给这个字段的默认值，
    那么可以使用路径操作装饰器的参数 response_model_exclude_unset=True
    """
    return items[item_id]


@response_router.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},  # 只返回这个路径操作装饰器中的字段
)
async def read_item_name(item_id: str):
    return items[item_id]


# 潜在的多个响应类型
class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type: str = "car"


class PlaneItem(BaseItem):
    type: str = "plane"
    size: int


items_base = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}


@response_router.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    return items_base[item_id]


# 响应状态码
@response_router.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}


@response_router.put("/items/", status_code=status.HTTP_201_CREATED)
async def update_item(name: str):
    return {"name": name}
