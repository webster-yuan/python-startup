# 路径参数测试代码
from enum import Enum

from fastapi import APIRouter, Path, Query
from typing import Annotated

path_param_router = APIRouter(prefix="/path_param", tags=["path_param"])


# ps: 顺序问题很重要，需要将特定的写在前面，需要匹配的放在后面
@path_param_router.get("/items/admin")  # 路径参数
async def read_items():
    return {"item_id": 1}


@path_param_router.get("/items/{item_id}")  # 路径参数
async def read_items(item_id: int):
    return {"item_id": item_id}


# 预定义值：Enum
class ModelName(str, Enum):
    """创建一个继承自 str 和 Enum 的子类，API文档知道值必须是 string 类型"""
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@path_param_router.get("/models/{model_name}")
async def read_models(model_name: ModelName):  # 枚举类带有类型注解的路径参数，路径参数是预定义的所以在交互式文档(/docs)中可以下拉框看到
    # 比较枚举成员
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    # 获取枚举值
    if model_name.value == ModelName.lenet.value:
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@path_param_router.get("/files/{file_path:path}")
async def read_file(file_path: str):
    """
    想接「多级目录」或「整段路径」→ 加 :path
    把 :path 去掉再访问 /files/a/b/c.txt 就会 404；加上就能完整拿到 "a/b/c.txt"
    """
    return {"file_path": file_path}


# 路径参数+数字验证
@path_param_router.get("/users/{user_id}")
async def read_users(
        user_id: Annotated[int, Path(title="User ID",
                                     ge=1,
                                     le=10
                                     )],
        q: Annotated[str | None, Query(alias="item-query")] = None
):
    """
    ge=1: 对路径参数进行数字验证，大于等于1
    le=10.5: 小于等于10.5，所以float类型也支持
    """
    result = {"user_id": user_id}
    if q is not None:
        result.update({"q": int(q)})

    return result
