from typing import Union

from fastapi import FastAPI,HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: Union[str, None] = None
    description: Union[str, None] = None
    price: Union[float, None] = None
    tax: float = 10.5
    tags: list[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}
@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]

@app.put("/items/{item_id}",response_model=Item)
async def update_items(item_id,item:Item):
    update_item_encoded=jsonable_encoder(item)
    items[item_id]=update_item_encoded
    return update_item_encoded

@app.patch("/items/{item_id}",response_model=Item)
async def patch_item(item_id:str,item:Item):
    stored_item=items.get(item_id)
    if not stored_item:
        raise HTTPException(status_code=404,detail="item not found")
    stored_item_data=jsonable_encoder(stored_item)
    # 将请求中包含的字段转化为字典,别的不包含的不会处理
    # update_data=item.dict(exclude_unset=True) dict已被替换为model_dump
    update_data=item.model_dump(exclude_unset=True)
    # 这行代码将原来的 item_id 条目中的数据与新的部分更新数据合并。
    # 只有在 update_data 中提供的字段才会被更新，未提供的字段将保留原有的值
    stored_item_data.update(update_data)
    items[item_id]=stored_item_data
    return stored_item_data

# exclude_unset 参数,接收部分更新

@app.patch("/items/{item_id}",response_model=Item)
async def patch_item(item_id:str,item:Item):
    stored_item_data=items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data=item.model_dump(exclude_unset=True)
    update_item=stored_item_model.copy(update=update_data)
    items[item_id]=jsonable_encoder(update_item)
    return update_item

# 使用pydantic的update参数
@app.patch("/items/{item_id}",response_model=Item)
async def update_items(item_id:str,item:Item):
    stored_item_data=items[item_id]
    stored_item_model=Item(**stored_item_data)
    update_data=item.model_dump(exclude_unset=True)
    update_item=stored_item_model.copy(update=update_data)
    items[item_id]=jsonable_encoder(update_item)
    return update_item