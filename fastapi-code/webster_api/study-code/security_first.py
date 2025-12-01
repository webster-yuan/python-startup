from typing import Annotated
from fastapi import FastAPI,Depends
from fastapi.security import OAuth2PasswordBearer


app=FastAPI()
# 此参数包含客户端（在用户浏览器中运行的前端）
# 将用于发送 username 和 password 以获取令牌的 URL(相对url,如果您的 API 位于 https://example.com/，则它将引用 https://example.com/token)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# oauth2_scheme 是一个示实例,也是一个可调用对象
# 基于依赖注入系统,将token作为str传递给路径操作函数

@app.get("/items/")
async def read_items(token:Annotated[str,Depends(oauth2_scheme)]):
    return {"token":token}

# 它将在请求中查找 Authorization 标头，
# 检查其值是否为 Bearer 加上某个令牌，并将令牌作为 str 返回。
# 如果它没有看到 Authorization 标头，或者其值没有 Bearer 令牌，它将直接以 401 状态码错误（UNAUTHORIZED）响应。
# 您甚至不必检查令牌是否存在以返回错误。您可以确信，如果您的函数被执行，它将在该令牌中拥有一个 str。
