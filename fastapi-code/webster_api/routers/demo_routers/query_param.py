# 查询参数
# 查询参数是以 ? 符号分隔的一组键值对，后面跟着 URL，并用 & 字符分隔
# http://127.0.0.1:8000/items/?skip=0&limit=10
import random

from fastapi import APIRouter, Query
from typing import Annotated, Literal

from pydantic import AfterValidator, BaseModel, Field

query_param_router = APIRouter(prefix="/query_param", tags=["query_param"])

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@query_param_router.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    # skip limit 在url是字符串，这里声明为int，会自动转为int并验证
    return fake_items_db[skip:skip + limit]


@query_param_router.get("/items/{item_id}")
async def get_item(item_id: str, q: str | None = None, short: bool = False):
    # 将默认值设置为 None 来声明可选的查询参数
    # str | None，相当于 Optional[str] 联合类型决定「类型范围」,3.10 以后直接用 str | None，别再写 Optional
    if q is not None:
        return {"item_id": item_id, "q": q}

    if short:
        # http://127.0.0.1:8000/items/foo?short=1
        # http://127.0.0.1:8000/items/foo?short=True
        # http://127.0.0.1:8000/items/foo?short=on
        # http://127.0.0.1:8000/items/foo?short=yes
        return {"item_id": item_id, "short": True}

    return {"item_id": item_id}


# 多个路径和查询参数，会根据名称进行匹配，不必太在乎顺序
@query_param_router.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, short: bool, q: str | None = None):
    item = {"item_id": item_id, "q": q}
    if q is not None:
        item.update({"q": int(q)})

    if not short:
        # 不给默认值时，就是查询路径中的必需查询参数
        item.update({"description": "This is an amazing item that has a long description"})

    return item


# 为查询参数添加【字符串】验证
@query_param_router.get("/items/")
async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")] = None):
    """
    Python 还有一个功能，允许使用 Annotated 将附加元数据放入这些类型提示中。
    q 是一个可以是 str 或 None 的参数，并且默认情况下它是 None
    q的默认值仍然是 None，在q是可选的情况下，希望Fastapi给到额外的验证，希望它最多包含 50 个字符
    Fastapi版本小于0.95.0时，老代码是 q: str | None = Query(default=None)，
    推荐使用 Annotated，当不使用fastapi调用时，如有一个必需的参数没有默认值，编辑器会通过错误提示，
    不传递必须参数，Python也会报错。
    使用旧的样式时，只有在内部操作运行时才会报错
    ps:
    1. 正则校验：
        ^：以以下字符开头，前面没有字符。
        fixedquery：具有确切的值 fixedquery。
        $：在此结束，fixedquery 之后没有其他字符。
    2. 拥有任何类型的默认值，包括 None，都会使参数成为可选的（非必需的）
    可以通过不声明默认值来使 q 查询参数成为必需的
    """
    results = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q is not None:
        results.update({"q": int(q)})

    return {"q": q}


# 查询参数列表多个值
# https://:8000/items/?q=foo&q=bar
@query_param_router.get("/multiple/users/")
async def read_users(q: Annotated[list[str] | None, Query(title="query users",
                                                          alias="user-query",
                                                          description="query users",
                                                          deprecated=True,
                                                          include_in_schema=False,
                                                          min_length=1)] = ["foo", "bar"]):
    """
    list[int] 将检查（并记录）列表的内容是整数。但仅使用 list 则不会。
    声明一个 alias，该别名将用于查找参数值
    deprecated=True 参数传递给 Query, 代表废弃了这个参数，在OpenAPI文档中会显示deprecated
    include_in_schema=False 将查询参数从生成的 OpenAPI 架构中排除（从而从自动文档系统中排除）
    """
    query_items = {"q": q}
    # {
    #   "q": [
    #     "foo",
    #     "bar"
    #   ]
    # }
    return query_items


# 自定义验证：这些验证无法通过上面显示的参数完成，可以使用一个自定义验证器函数，它在正常验证之后应用
# AfterValidator
data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}


def check_valid_id(item_id: str):
    """
    使用 value.startswith() 的字符串可以接受一个元组，它将检查元组中的每个值
    """
    if not item_id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')

    return item_id


@query_param_router.get("/validator/items/")
async def read_validator_items(
        item_id: Annotated[str | None, AfterValidator(check_valid_id)] = None
):
    if id is not None:
        item = data.get(item_id)
    else:
        item_id, item = random.choice(list(data.items()))
        """
        使用 data.items()，我们得到一个 可迭代对象，其中包含每个字典项的键和值元组
        使用 list(data.items()) 将此可迭代对象转换为一个真正的 list
        使用 random.choice()，我们可以从列表中获取一个随机值，因此，我们将获得一个包含 (id, name) 的元组
        然后我们将元组的这两个值分配给变量 id 和 name
        """
    return {"id": item_id, "name": item}


# 查询参数模型
class FilterParam(BaseModel):
    # 客户端尝试在查询参数中发送一些额外的数据
    model_config = {"extra": "forbid"}
    
    # 用 Pydantic 的 Field 在 Pydantic 模型内部声明验证和元数据
    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@query_param_router.get("/filter/items/")
async def filter_items(
        filter_query: Annotated[FilterParam, Query()],
):
    """
    FastAPI 将会从请求中的查询参数中提取每个字段的数据，并为您提供定义的 Pydantic 模型
    """
    pass
