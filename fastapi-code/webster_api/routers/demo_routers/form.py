from fastapi import APIRouter, Form
from typing import Annotated

from pydantic import BaseModel

form_router = APIRouter(prefix="form", tags=["form"])


@form_router.post("/loginV1")
async def login(
        username: Annotated[str, Form()],
        password: Annotated[str, Form()]
):
    return {"username": username, "password": password}


# 表单模型
class FormData(BaseModel):
    username: str
    password: str

    model_config = {"extra": "forbid"}  # 禁止额外的表单字段


@form_router.post("/loginV2")
async def login_v2(
        data: Annotated[FormData, Form()]
):
    return {"username": data.username, "password": data.password}
