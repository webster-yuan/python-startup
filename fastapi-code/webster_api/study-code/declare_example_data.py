from fastapi import FastAPI,Body
from pydantic import BaseModel, Field
from typing import Union, Annotated

app = FastAPI()


# 1. 可以为 Pydantic 模型声明 examples，这些示例将被添加到生成的 JSON Schema 中
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "foo",
                    "description": "a very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }


@app.put("/items/{item_id}")
async def update_item1(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


# 2. 使用 Pydantic 模型中的 Field() 时，您也可以声明额外的 examples
class Item2(BaseModel):
    name: str = Field(examples=["foo"])
    description = Union[str, None] = Field(default=None, examples=["nice item"])
    price: float = Field(examples=[35.4])
    tax: Union[float, None] = Field(default=None, examples=[3.2])


@app.put("/items/{item_id}")
async def update_item2(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

# 3. 带有examples的body
# 这些示例将成为该主体数据内部的 JSON Schema 的一部分。
class Item2(BaseModel):
    name:str
    decription:Union[str,None]=None
    price:float
    tax:Union[float,None]=None
    
@app.put("/items/{item_id}")
async def update_item(
    item_id:int,
    item:Annotated[
        Item2,
        Body(
            examples=[
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ],
        )
    ]
):
    results = {"item_id":item_id,"item":item}
    return results
    