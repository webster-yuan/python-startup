# 路径参数获取和数字验证


from fastapi import FastAPI, Query, Path
from typing import Annotated, Union

app = FastAPI()


# 查询参数使用Query 路径参数使用Path
@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[Union[str, None], Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# 不使用Annotated时,需要注意按需排列参数,但是FastAPI并不关注顺序
# 查询参数可以不用Query当你不需要时,但是需要对路径参数使用Path
# 因为python不允许把提供默认值的参数放在没有的之前,所以要调换顺序
# 这个默认值:是因为python认为Path对象作为了一个默认值
# Fastapi习惯于将第一个参数认为是路径参数,但是FastAPI并不关注顺序去匹配
@app.get("/items/{item_id}")
async def read_items_v1(q: str, item_id: int = Path(title="ID of item to get")):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
        return results


# 第一个参数传* ,告知python后续参数应该作为关键词参数调用kwargs,
# 函数定义def func(a,b)
# 函数调用:func(a=a,b=b)此时就会忽略顺序以及python对于默认值顺序的要求
@app.get("/items/{item_id}")
async def read_items_v1(*, item_id: int = Path(title="ID of item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
        return results


# (最好使用)当使用Annotated时不会报错,因为没有将 Path添加的元数据生成的对象 作为参数的默认值,python不会报错
@app.get("/items/{item_id}")
async def read_items_v2(
    item_id: Annotated[int, Path(title="ID of item to get")], q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
        return results

# 数字验证:大于 等于greater than or equal 1
@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int,Path(title="id of item to get",ge=1)],
    q:str
):
    results = {"item_id":item_id}
    if q:
        results.update({"q":q})
    return results

# gt: greater than
# le: less than or equal
@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int,Path(title="id of item to get",ge=0,le=1000)],
    q:str
):
    results = {"item_id":item_id}
    if q:
        results.update({"q":q})
    return results

# float lt: less than gt: greater than
@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int,Path(title="id of item to get",ge=0,le=1000)],
    q:str,
    size: Annotated[float,Query(gt=0,lt=10.5)]
):
    results = {"item_id":item_id}
    if q:
        results.update({"q":q})
    return results
