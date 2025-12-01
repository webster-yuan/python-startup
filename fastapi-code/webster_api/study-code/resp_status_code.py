# 响应状态码

from fastapi import FastAPI,status

app=FastAPI()

# status_code 装饰器方法参数
# 声明用于响应的HTTP状态码
@app.post("/items/", status_code=201)
async def create_item_v1(name:str):
    return {"name":name}


# 不必记住状态码的含义,因为fastapi.status中的便捷变量可以使用
@app.post("/items/",status_code=status.HTTP_201_CREATED)
async def create_item_v2(name:str):
    return {"name":name}
