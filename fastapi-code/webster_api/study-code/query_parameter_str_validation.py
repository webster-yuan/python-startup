# 查询参数和字符串验证

from typing import Union, List
from fastapi import FastAPI, Query
from typing_extensions import Annotated

app = FastAPI()


@app.get("/items/")
async def read_items(q: Union[str, None] = None):
    result = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        result.update({"q": q})
    return result


# 附加验证,q长度不超过50个字符
# 在 q 参数的 Annotated 中添加 Query => 对查询参数进行额外的验证
@app.get("/items/")
async def read_items2(q: Annotated[Union[str, None], Query(max_length=50)] = None):
    result = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        result.update({"q": q})
    return result


# 不使用Annotated,使参数可选，默认值为 None
@app.get("/items/")
async def read_items2_old(q: Union[str, None] = Query(default=None, max_length=50)):
    result = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        result.update({"q": q})
    return result


# 注: 在使用Annotated,将Query对象作为参数时不允许使用default参数


# 更多验证
# 添加最小值校验
@app.get("/items/")
async def read_items3(
    q: Annotated[Union[str, None], Query(max_length=50, min_length=3)] = None
):
    result = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        result.update({"q": q})
    return result


# 正则表达式校验,提取参数时使用
# ^: 以以下字符开头，前面没有字符。
# fixedquery: 具有确切的值 fixedquery。
# $: 在此结束，fixedquery 后面没有更多字符。
# regex参数已经过时,正则就使用pattern
@app.get("/items/")
async def read_items4(
    q: Annotated[
        Union[str, None], Query(max_length=50, min_length=3, pattern="^fixedquery$")
    ] = None
):
    result = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        result.update({"q": q})
    return result


# 默认值
@app.get("/items/")
async def read_items4(
    q: Annotated[str, Query(max_length=50, min_length=3)] = "fixedquery"
):
    result = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        result.update({"q": q})
    return result


# 设置为必需的参数,将默认值去掉即可
@app.get("/items/")
async def read_items_needy(q: Annotated[str, Query(min_length=3)]):
    results = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        results.update({"q": q})
    return results


# ... 明确声明一个值是必填的,直接告知FastAPI
@app.get("/items/")
async def read_items_needy(q: Annotated[str, Query(min_length=3)] = ...):
    results = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        results.update({"q": q})
    return results


# 一个值可以为None,但是必须填写
@app.get("/items/")
async def read_items_needy(q: Annotated[Union[str, None], Query(min_length=3)] = ...):
    results = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        results.update({"q": q})
    return results


# 查询参数列表->query多个参数时,可以使用列表接收
# http://localhost:8000/items/?q=foo&q=bar
@app.get("/items/")
async def read_items(q: Annotated[Union[List[str], None], Query()] = None):
    query_items = {"q": q}
    return query_items


# {
#   "q": [
#     "foo",
#     "bar"
#   ]
# }


# 查询参数列表 携带多个默认值
@app.get("/items/")
async def read_items(q: Annotated[Union[List[str], None], Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items


# 使用list 不会强制检查每个元素必须是str
@app.get("/items/")
async def read_items(q: Annotated[Union[list, None], Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items


# Query 声明更多元数据
@app.get("/items")
async def read_items(
    q: Annotated[
        Union[str, None],
        Query(
            title="query string",
            min_length=3,
            description="Query string for the items to search in the database that have a good match",
        ),
    ] = None
):
    results = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        results.update({"q": q})
    return results


# Query 别名参数 alias
@app.get("/items/")
async def read_items(q: Annotated[Union[str, None], Query(alias="item-query")] = None):
    results = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        results.update({"q": q})
    return results


# Query 弃用参数
@app.get("/items")
async def read_items(
    q: Annotated[
        Union[str, None],
        Query(
            title="query string",
            min_length=3,
            description="Query string for the items to search in the database that have a good match",
            deprecated=True,  # 弃用参数
        ),
    ] = None
):
    results = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
    if q:
        results.update({"q": q})
    return results


# 彻底从自动生成的 openAPI 文档中不显示
@app.get("/items/")
async def read_items(
    hidden_query: Annotated[Union[str, None], Query(include_in_schema=False)] = None
):
    if hidden_query:
        return {}
    else:
        return {}
