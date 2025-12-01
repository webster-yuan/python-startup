from fastapi import Body, FastAPI, Path
from pydantic import BaseModel
from typing import Any, Dict, Union, Annotated
from app.schemas.user import User as BaseUser

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class User(BaseUser):
    username: str
    full_name: Union[str, None] = None


# dict.update(): 如果原字典中不存在新字典的某个键，则该键值对会被添加到原字典中。

# 1. 主体参数Item
# fastapi会注意到主题参数是Pytantic模型Item,那么他会期待一个JSON主体
# {
#     "name": "Foo",
#     "description": "The pretender",
#     "price": 42.0,
#     "tax": 3.2
# }


@app.put("/items/{item_id}")
async def update_item_v1(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: Union[str, None] = None,
    item: Union[Item, None] = None,
):
    results : Dict[str, Any] = {"item_id": item_id}
    if q:
        results.update({"q": q})
        
    if item:
        results.update({"item": item})
        
    return results


# 2. 多个主体参数
# fastapi会注意到多个主体参数,会使用参数名称作为键(key->字段名称),并且期望如下主体
# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     },
#     "user": {
#         "username": "dave",
#         "full_name": "Dave Grohl"
#     }
# }
@app.put("/items/{item_id}")
async def update_item_v3(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results


# 3. 添加主体参数
# 避免被认为是查询参数
# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     },
#     "user": {
#         "username": "dave",
#         "full_name": "Dave Grohl"
#     },
#     "importance": 5
# }
@app.put("/items/{item_id}")
async def update_item_v4(item_id: int, item: Item, user: User,
                      importance:Annotated[int,Body()]
):
    results = {"item_id": item_id, "item": item, "user": user,"importance":importance}
    return results


@app.put("/items/{item_id}")
async def update_item_v5(item_id: int, item: Item, user: User,
                      importance:Annotated[int,Body()],
                      q:Union[str,None]=None
):
    results = {"q":q,"item_id": item_id, "item": item, "user": user,"importance":importance}
    return results

# 4. 嵌入单个主体参数
# 如果你希望fastapi期望的json主体如下:(添加了字段名作为key)
# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     }
# }
@app.get("/items/{item_id}")
async def update_item_v6(item_id:int,item:Annotated[Item,Body(embed=True)]):
    results= {"item_id":item_id,"item":item}
    return results