from typing import Annotated,Union
from fastapi import FastAPI,Depends


app=FastAPI()

# 可以看做是一个没有装饰器的路径操作函数
async def common_parameters(
    q:Union[str,None]=None,
    skip:int=0,
    limit:int=100
):
    return {"q":q,"skip":skip,"limit":limit}

# 传入的depends是一个参数,此参数必须类似函数,不要加上(),只需要将其作为参数传递即可
# 该函数以与 路径操作函数 相同的方式接收参数
# 结果返回并分配给路径操作函数中的参数
@app.get("/items")
async def read_items(commons:Annotated[dict,Depends(common_parameters)]):
    return commons

@app.get("/users/")
async def read_users(commons:Annotated[dict,Depends(common_parameters)]):
    return commons

# 共享Annotated依赖项:将Annotated值存储在变量中,在多个地方使用
# Python中叫 类型别名,fastapi是基于Python标准(包括Annotated),所以可以使用
CommonsDep = Annotated[dict,Depends(common_parameters)]

@app.get("/items/")
async def read_items(commons:CommonsDep):
    return commons

@app.get("/users/")
async def read_users(commons:CommonsDep):
    return commons

