# 使用密码和 Bearer 的简单 OAuth2

# scope 范围,是客户端发送的一个表单字段,
# 是一个长字符串,其中包含以空格分隔的范围,每个范围只是一个字符串(不包含空格)
# 通常用于声明特定的安全权限,例如users:read users:write,具体细节不关注


# 1. 获取username和password
from typing import Union, Annotated
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

app = FastAPI()


def fake_hash_password(password: str):
    return "fakehashed" + password

# OAuth2PasswordBearer 根据url提取Bearer Token令牌
# Depends()会让Fastapi自动从请求的Authorization头中解析出令牌
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


class UserInDB(User):
    hashed_password: str


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)


def fake_decode_token(token):
    user = get_user(fake_users_db, token)
    return user


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    # 验证令牌合法性逻辑
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invaild authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
            # 任何 HTTP（错误）状态代码 401“未授权”都应该返回 WWW-Authenticate 标头
        )
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# OAuth2PasswordRequestForm 是一个类依赖项,声明了一个表单主体,包含
# username password 可选的scope(由空格作为分隔符组成的字符串) 可选的grant_type
# OAuth2 规范实际上要求一个名为 grant_type 的字段，其固定值为 password，但 OAuth2PasswordRequestForm 并没有强制执行
# 如果您需要强制执行，请使用 OAuth2PasswordRequestFormStrict 代替 OAuth2PasswordRequestForm
@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": user.username, "token_type": "bearer"}
    # 由于我们使用的是“Bearer”令牌，因此令牌类型应为“bearer”。

@app.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user

# UserInDB(**user_dict)相当于
# UserInDB(
#     username = user_dict["username"],
#     email = user_dict["email"],
#     full_name = user_dict["full_name"],
#     disabled = user_dict["disabled"],
#     hashed_password = user_dict["hashed_password"],
# )