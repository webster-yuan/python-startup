# 将多个参数传递给 路径操作装饰器 ,而不是路径操作函数

# 1. 响应状态码

from typing import Union
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: set[str] = set()


@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create(item: Item):
    return item

# 2. 标签 列表,但是通常是一个.它们将添加到 OpenAPI 模式中，并由自动文档界面使用
@app.post("/items/",response_model=Item,tags=["items"])
async def create(item: Item):
    return item

@app.get("/items/",tags=["items"])
async def read_items(item: Item):
    return item

@app.get("/users/",tags=["users"])
async def read_users():
    return [{"username":"yw"}]

# 3. 代枚举的标签
from enum import Enum
class Tags(Enum):
    items="items"
    users="users"

@app.get("/items/",tags=[Tags.items])
async def get_items():
    return ["portal gun","plumbus"]

@app.get("users/",tags=[Tags.users])
async def read_users():
    return ["rick","morty"]

# 4. 添加摘要(summary) 描述(description)
@app.post(
    "/items",
    response_model=Item,
    summary="Create an item",
    description="Create an item with all the information, name, description, price, tax and a set of unique tags"
)
async def create_item(item:Item):
    return item

# 5. 编写文档字符串(用于交互文档显示,支持markdown格式)
@app.post("/items/", response_model=Item, summary="Create an item")
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item

# 6. 响应描述
@app.post("/items/", response_model=Item, summary="Create an item",
          response_description="the created item")
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item

# 7. 弃用路径操作
@app.get("/elements/",tags=["items"],deprecated=True)
async def read_elements():
    return [{"item_id":"foo"}]
    