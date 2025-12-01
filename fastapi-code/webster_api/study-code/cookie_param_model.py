
from fastapi import FastAPI,Cookie
from pydantic import BaseModel
from typing import Union,Annotated


app=FastAPI()

class Cookies(BaseModel):
    session_id:str
    fatebook_tracer :Union[str,None]=None
    googall_tracker:Union[str,None]=None
    
# **FastAPI** 将从请求中收到的 **Cookie** 中 **提取** 每个字段的数据，并为您提供您定义的 Pydantic 模型。
@app.get("/items")
async def read_items(cookies:Annotated[Cookies,Cookie()]):
    return cookies

# 2. 限制接收到的Cookie,只能是类中的两种
class Cookies(BaseModel):
    model_config={"extra":"forbid"}
    session_id:str
    fatebook_tracer :Union[str,None]=None
    googall_tracker:Union[str,None]=None
    