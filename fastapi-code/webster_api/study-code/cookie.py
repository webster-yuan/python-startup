from fastapi import FastAPI,Cookie
from typing import Annotated,Union


app=FastAPI()
# 使用 Cookie 声明 cookie，使用与 Query 和 Path 相同的通用模式。
# Cookie 是 Path 和 Query 的“姐妹”类。它也继承自相同的公共 Param 类。
@app.get("/items/")
async def read_items(ads_id:Annotated[Union[str,None],Cookie()]=None):
    return {"ads":ads_id}
