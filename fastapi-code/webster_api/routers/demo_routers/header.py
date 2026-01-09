from fastapi import APIRouter, Header
from typing import Annotated

from pydantic import BaseModel

header_router = APIRouter(prefix="/header", tags=["header"])


@header_router.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}


class CommonHeaders(BaseModel):
    model_config = {"extra": "forbid"}
    
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@header_router.get("/common-headers/")
async def read_common_headers(
        headers: Annotated[CommonHeaders, Header(convert_underscores=False)]
):
    """
    如果你在代码中有一个 header 参数 save_data，
    预期的 HTTP header 将是 save-data，
    并且在文档中也会显示为 save-data。
    如果出于某种原因你需要禁用此自动转换，你也可以为 header 参数的 Pydantic 模型执行此操作。
    """
    return headers
