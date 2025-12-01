from typing import List, Union, Any
from fastapi import FastAPI, Response
from pydantic import BaseModel, EmailStr
from fastapi.responses import JSONResponse, RedirectResponse
from app.auth import get_password_hash

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: list[str] = []


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/")
async def read_items_v1() -> list[Item]:
    return [Item(name="Portal Gun", price=42.0), Item(name="Plumbus", price=32.0)]


# 2. 希望将数据声明为Pydantic模型,让其检查类型和数据正确性
# response_model:
# 1. 告诉 FastAPI 你期望从你的路径操作函数返回哪种数据模型
# 2. 自动将输出数据序列化成定义的模型格式，确保输出的响应遵循特定的结构和数据类型
@app.post("/items/", response_model=Item)
async def create_item2(item: Item) -> Any:
    return item


@app.get("/items/", response_model=list[Item])
async def read_items_v2() -> Any:
    return [Item(name="Portal Gun", price=42.0), Item(name="Plumbus", price=32.0)]


# 3. response_model优先级 > 函数返回值
@app.get("/items/", response_model=list[Item])
async def read_items_v3() -> List[Item]:
    return [Item(name="Portal Gun", price=42.0), Item(name="Plumbus", price=32.0)]


@app.get("/items/", response_model=None)  # 禁用为该路径操作创建响应模型
async def read_items_v4() -> List[Item]:
    return [Item(name="Portal Gun", price=42.0), Item(name="Plumbus", price=32.0)]


# 4. 返回相同的输入数据 : 对于输入输出模型要区分开,不能使用同一个模型
# 如下例子就可能导致每次都会将敏感的明文密码都返回,
# 在使用这个模型在不同的路由时
class UserInModel(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


@app.post("/user/")
async def create_user_v1(user: UserInModel) -> UserInModel:
    return user


# 另外定义一个pydantic模型,告诉fastapi只会将这个模型的数据筛选出来并返回
class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


@app.post("/user/", response_model=UserOut)
async def create_user_v2(user: UserInModel) -> Any:
    return user


# response_model 类型和函数返回值类型不一致,可能会导致编辑器报错
# 这也意味着我们无法从编辑器和工具中获得检查函数返回类型的支持
# 5. 使用继承的方式解决问题,实现数据过滤


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserIn(BaseUser):
    password: str


# 结果: 带有 工具支持 的类型注释 + 数据过滤 功能实现
@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user


# 6. 其他返回类型注释
# 返回 类型注释 是 类的子类,编辑器会很高兴
@app.get("/portal")
async def get_portal_v1(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})


@app.get("/teleport")
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")


# 失败案例:类型注释类似于联合Union,其中一个或多个类型不是有效的 Pydantic 类型
@app.get("/portal")
async def get_portal(teleport: bool = False) -> Union[Response, dict]:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}


# 忽略响应模型中字段的默认值
class Item2(BaseModel):
    name: str
    decription: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_items2(item_id: str):
    return items[item_id]

@app.get(
    "/items/{item_id}/name",
    response_model=Item2,
    response_model_include={"name","description"}
)
async def read_item_name(item_id: str):
    return items[item_id]
    
@app.get("/items/{item_id}/public", response_model=Item2, response_model_exclude={"tax"})
async def read_item_public_data(item_id: str):
    return items[item_id]

# 虽然可以使用 respnse_model_include response_model_exclude控制返回哪些字段
# 但是还是建议使用类继承的方式处理哪些字段可以返回,针对特殊场景,可以使用这两个
# 路径操作装饰器参数处理
# 即使声明respnse_model_include时使用的是list tuple ,fastapi也会自动处理为set