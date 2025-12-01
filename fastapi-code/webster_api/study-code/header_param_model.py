from fastapi import FastAPI, Header
from typing import Union, Annotated
from pydantic import BaseModel

app = FastAPI()


class CommonHeaders(BaseModel):
    model_config={"extra":"forbid"} # 禁止传入额外的头部参数
    
    host: str
    save_data: bool
    if_modified_since: Union[str, None] = None
    traceparent: Union[str, None] = None
    x_tag: list[str] = []


@app.get("/items/")
async def read_items(headers:Annotated[CommonHeaders,Header()]):
    return headers
