from typing import Annotated, Union

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

# 安全
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# 数据模型
class User(BaseModel):
    username:str
    email :Union[str,None]=None
    full_name:Union[str,None]=None
    disabled:Union[bool,None]=None
   
# 实用程序函数 
def fake_decode_token(token):
    return User(
        username=token+"fakedecoded",
        email="john@example.com",
        full_name="john Doe"
    )

# 获取用户
# 可能涉及到访问数据库获取用户密码,所以建议设置为异步async
async def get_current_user(token:Annotated[str,Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user

# 路径操作函数-> 注入当前用户
@app.get("/users/me")
async def read_users_me(current_user:Annotated[User,Depends(get_current_user)]):
    return current_user

