# API请求体使用Pydantic
from typing import Annotated

from pydantic import BaseModel, HttpUrl, Field
from fastapi import APIRouter, Path, Body

req_body_router = APIRouter(prefix="/req_body", tags=["req_body"])


class Item(BaseModel):
    """数据模型声明为一个继承自 BaseModel 的类，对所有属性使用标准的 Python 类型"""
    name: str
    description: str | None = None  # 存在默认值，可选参数
    price: float
    tax: float | None = None  # 存在默认值，可选参数


@req_body_router.post("/items/")
async def create_item(item: Item):
    """
    1. 读取请求体为 JSON。
    2. 转换相应的数据类型（如果需要）。
    3. 验证数据。
        如果数据无效，它将返回一个清晰明了的错误，精确指出哪里以及是什么数据不正确。
    4. 将收到的数据赋值给你在参数 item 中。
        由于你在函数中将其声明为 Item 类型，你还将获得所有编辑器支持（自动完成等），包括所有属性及其类型。
    5. 为你的模型生成 JSON Schema 定义，如果适合你的项目，你也可以在其他任何地方使用它们。
    6. 这些模式将构成生成的 OpenAPI 模式的一部分，并被自动文档 UI 使用
    """
    item_dict = item.model_dump()
    # 把 Pydantic 模型实例 → 转成 Python 原生字典
    # 后续你可以自己 json.dumps() 或让 FastAPI 自动序列化

    # 可以直接访问模型对象的所有属性
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})

    return item_dict


@req_body_router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    """
    1. 如果参数也声明在[路径]中，则将其用作路径参数。
    2. 如果参数是单一类型（如 int、float、str、bool 等），则将其解释为查询参数。
    3. 如果参数被声明为Pydantic 模型的类型，则将其解释为请求体
    FastAPI 将识别出和路径参数item_id匹配的函数参数item_id将从路径中获取
    而声明为 Pydantic 模型 的函数参数将*从请求体中获取
    """
    result = {"item_id": item_id, **item.model_dump()}
    if q is not None:
        # 查询参数
        result.update({"q": int(q)})

    return result


class User(BaseModel):
    username: str
    full_name: str | None = None


# 混合 Path, Query 和 body 参数
@req_body_router.post("/items/{item_id}")
async def create_item(
        item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
        q: str | None = None,
        item: Item | None = None,
        user: User | None = None,
):
    """
    FastAPI 会注意到函数中有多个 body 参数（有两个参数是 Pydantic 模型）
    它将使用参数名称作为 body 中的键（字段名称），并期望一个 body，例如
    {
        "item": {
            "name": "Foo",
            "description": "The pretender",
            "price": 42.0,
            "tax": 3.2
        },
        "user": {
            "username": "dave",
            "full_name": "Dave Grohl"
        }
    }
    它将执行复合数据的验证，并将其记录在 OpenAPI schema 和自动文档中
    """
    results = {"item_id": item_id}
    if q:
        results.update({"q": int(q)})

    if item:
        results.update({"item": item})

    if user:
        results.update({"user": user})

    return results


@req_body_router.put("/req_body/items/{item_id}")
async def req_body_update_item(
        item_id: int,
        item: Item,
        user: User,
        importance: Annotated[int, Body()],
        q: str | None = None,
):
    """
    扩展之前的模型，你可能决定在同一个 body 中除了 item 和 user 之外，还有一个键 importance。
    如果你按原样声明它，因为它是一个单个值，FastAPI 将假设它是一个 query 参数。
    但是你可以指示 FastAPI 使用 Body 将其视为另一个 body 键，请求体会如下：
    {
        "item": {
            "name": "Foo",
            "description": "The pretender",
            "price": 42.0,
            "tax": 3.2
        },
        "user": {
            "username": "dave",
            "full_name": "Dave Grohl"
        },
        "importance": 5
    }
    q 多添加一个查询参数
    """
    results = {
        "item_id": item_id,
        "item": item,
        "user": user,
        "importance": importance,
        "q": int(q)
    }
    return results


@req_body_router.get("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    """
    如果你希望它期望一个带有键 item 的 JSON，并且其内容在 item 里面，就像声明额外的 body 参数时那样，你可以使用特殊的 Body 参数 embed
    不加上，请求体内容为：
    {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
    加上：
    {
        "item": {
            "name": "Foo",
            "description": "The pretender",
            "price": 42.0,
            "tax": 3.2
        }
    }
    """
    results = {"item_id": item_id, "item": item}
    return results


# 请求体嵌套类型
class Image(BaseModel):
    url: HttpUrl  # 使用Pydantic的HttpUrl类型，字符串将被检查以确保它是有效的 URL
    name: str


class NestedItem(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None


@req_body_router.put("/nested/items/{item_id}")
async def update_item(item_id: int, item: NestedItem):
    """
    {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2,
        "tags": ["rock", "metal", "bar"],
        "image": {
            "url": "http://example.com/baz.jpg",
            "name": "The Foo live"
        }
    }
    """
    results = {"item_id": item_id, "item": item}
    return results


# 声明请求示例数据
class ExampleItem(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    # 这些额外信息将按原样添加到该模型的 JSON Schema 输出中，并将在 API 文档中使用
    # 使用 model_config 属性，该属性接受一个 dict
    # 可以使用包含任何您希望显示在生成的 JSON Schema 中的额外数据的 dict 来设置 "json_schema_extra"，包括 examples
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }


@req_body_router.put("/examples/items/{item_id}")
async def examples_update_item(item_id: int, item: ExampleItem):
    results = {"item_id": item_id, "item": item}
    return results


# Field 的附加参数 examples 参数
class FieldExampleItem(BaseModel):
    name: str = Field(examples=["Foo"])
    description: str | None = Field(default=None, examples=["A very nice Item"])
    price: float = Field(examples=[35.4])
    tax: float | None = Field(default=None, examples=[3.2])


@req_body_router.put("/field_examples/items/{item_id}")
async def field_examples_update_item(item_id: int, item: FieldExampleItem):
    results = {"item_id": item_id, "item": item}
    return results


# 带有(单个，多个) examples 的 Body()
class OnlyItem(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@req_body_router.put("/multiple_example_body/items/{item_id}")
async def multiple_example_body_update_item(
        item_id: int,
        item: Annotated[
            Item,
            Body(
                examples=[
                    {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                    {
                        "name": "Bar",
                        "price": "35.4",
                    },
                    {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                ],
            ),
        ],
):
    results = {"item_id": item_id, "item": item}
    return results
