
# 某些情况下,路径操作函数并不需要获取依赖的返回值,但是还想再这之前执行这些步骤
# 可以将dependencies的list添加到路径操作装饰器中,而不是路径操作函数的参数列表中

from typing import Annotated
from fastapi import Depends, FastAPI, Header, HTTPException


app=FastAPI()

async def verify_token(x_token:Annotated[str,Header()]):
    if x_token!="fake-super-secret-token":
        raise HTTPException(status_code=400,detail="X-Token header invalid")
    
async def verify_key(x_key:Annotated[str,Header()]):
    if x_key!="fake-super-secret-key":
        raise HTTPException(status_code=400,detail="X-Key header invalid")
    return x_key

# 依赖列表 返回值也不会传给路径操作函数
@app.get("/items/",dependencies=[Depends(verify_token),Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]

