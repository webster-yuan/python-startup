from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


# 使用None使得这个参数是可选的
# Union[str,None]这个参数可以为None,针对多类型处理
# Union的使用只是为了满足代码的编写,fastapi并不会识别Union
# 不必太纠结Union[None]在默认值这里的使用,因为主要使用Union是针对两个实际的类型之间
# Union[str,int]
class Item(BaseModel):
    name: str
    desc: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post("/items/")
async def create_item_v1(item: Item):
    return item


@app.post("/items/create_item")
async def create_item_v2(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item


# 请求体+路径参数
# fastapi会对函数参数列表中,动识别出与路径参数匹配路径参数,从路径中获取
# 声明为Pydantic模型的函数参数从请求体中获取
@app.put("/items/{item_id}")
async def update_item_v1(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


# 请求体body+路径path+查询参数query
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result

#
# **item.dict() 是将 item.dict() 返回的字典展开为独立的键值对，
# 并将它们添加到目标字典中,实际的数据例子如下:
# result = {
#     "item_id": 123, 
#     "name": "Apple", 
#     "price": 2.5
# }
