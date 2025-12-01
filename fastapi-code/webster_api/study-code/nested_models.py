# 感谢Pydantic,可以使得主体参数支持嵌套


from fastapi import FastAPI
from typing import Union, List
from pydantic import BaseModel, HttpUrl

app = FastAPI()


# 1. 列表字段
class Item1(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    # 1.1 列表写法区别
    tags1: list = []  # 使 tags 成为一个列表，尽管它没有声明列表元素的类型
    tags2: List[str] = []  # 约束类型为str 3.9之前版本
    tags3: list[str] = []  # 约束类型为str 3.9开始版本
    # 1.2 (业务)标签不应该重复,更换数据结构
    tags4: set[str] = set()  # 标签不应该重复


# 2. 自定义子模型嵌套作为属性
class Image1(BaseModel):
    url: str
    name: str


# 使用更专业(适合业务场景以及有效性校验)的字段类型替换str
class Image(BaseModel):
    url: HttpUrl
    name: str


class Item2(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    image: Union[Image, None] = None


# 3. 包含子模型列表
# fastapi期待如下JSON主体
# {
#     "name": "Foo",
#     "description": "The pretender",
#     "price": 42.0,
#     "tax": 3.2,
#     "tags": [
#         "rock",
#         "metal",
#         "bar"
#     ],
#     "images": [
#         {
#             "url": "http://example.com/baz.jpg",
#             "name": "The Foo live"
#         },
#         {
#             "url": "http://example.com/dave.jpg",
#             "name": "The Baz"
#         }
#     ]
# }
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    image: Union[List[Image], None] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


# 4. 深度嵌套
class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    items: list[Item]


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer


# 5. 纯列表的主体
@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    # 支持自动补全
    for image in images:
        image.url = ""
        image.name = ""
    return images

# 6. 任意dict主体
@app.post("/index-weights/")
async def create_index_weights(weights:dict[int,float]):
    return weights