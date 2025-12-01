# 注意区分一下路径参数和查询参数

# 查询参数Query
# 默认值
from enum import Enum
from typing import Union
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


# 可选参数 将默认值设置为None
# fastapi能够自动识别出 item_id 为路径参数,q是查询参数
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# 查询参数类型转换 bool
# http://127.0.0.1:8000/items/foo?short=1
# http://127.0.0.1:8000/items/foo?short=True
# http://127.0.0.1:8000/items/foo?short=true
# http://127.0.0.1:8000/items/foo?short=on
# http://127.0.0.1:8000/items/foo?short=yes
# 都可以转换为bool类型
@app.get("/items/{item_id}")
async def read_item2(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"desc": "this item has a long desc"})
    return item


# 多个路径参数和查询参数
# fastapi能够区分出来
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None], short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update({"desc": "long item"})
    return item


# 必须查询参数:只需要不声明任何默认值
@app.get("/items/{item_id}")
async def read_user_item2(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item


@app.get("/items/{item_id}")
async def read_user_item3(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
):
    item = {"item_id": item_id, "needy": needy}
    return item
# needy，一个必需的 str。
# skip，一个默认值为 0 的 int。
# limit，一个可选的 int。

# 定义枚举类型
class FruitEnum(str,Enum):
    apple="apple"
    banana="banana"
# 在路径参数中使用Enum,限制前段传来的参数值只能是枚举其中之一
@app.get("/fruis/{fruit_name}")
def get_fruit(fruit_name:FruitEnum):
    return {"fruit_name":fruit_name}
