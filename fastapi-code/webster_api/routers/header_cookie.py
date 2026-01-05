from fastapi import APIRouter, Cookie
from typing import Annotated

from pydantic import BaseModel

header_cookie_router = APIRouter(prefix="/header_cookie", tags=["header"])


@header_cookie_router.get("/header/cookie")
async def get_header_cookie(
        ads_ids: Annotated[str | None, Cookie()] = None,
):
    """
    FastAPI 的 Cookie() 就是去解析 HTTP 请求头里的 Cookie: 字段（注意大小写，请求头是 Cookie，响应头是 Set-Cookie）。
    浏览器在发请求时会自动把当前域下所有未过期的 cookie 用 ;  拼接成一行放进请求头，例如：
    Cookie: ads_id=abc123; session=xyz789; theme=dark
    FastAPI 拿到这行后，
    单独额外内部自行处理逻辑：!!!
    -> 按 ;  分割，再按 = 提取键值，最后把键名匹配到参数 ads_id 注入给你的函数。
    """
    return {"ads_ids": ads_ids}


# 在Pydantic 模型中声明您需要的cookie参数，然后将参数声明为 Cookie
class Cookies(BaseModel):
    # 禁止额外的Cookie字段
    model_config = {"extra": "forbid"}
    
    session_id: str
    fate_book_tracer: str | None = None


@header_cookie_router.get("/items/")
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies
