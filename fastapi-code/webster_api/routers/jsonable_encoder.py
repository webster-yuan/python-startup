from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from datetime import datetime

from sqlalchemy.sql.annotation import Annotated

jsonable_encoder_router = APIRouter(prefix="json_encoder", tags=["json_encoder"])

fake_db = {}


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None


@jsonable_encoder_router.post("/items")
async def create_item(item_id: str, item: Annotated[Item, Body()]):
    """
    假设您有一个 fake_db 数据库，它只接收 JSON 兼容的数据。
    例如，它不接收 datetime 对象，因为这些对象与 JSON 不兼容。
    因此，datetime 对象必须转换为一个包含 ISO 格式数据的 str
    同样，此数据库不会接收 Pydantic 模型（带有属性的对象），而只接收 dict
    可以使用 jsonable_encoder 来实现此目的,
    它接收一个对象，例如 Pydantic 模型，并返回一个 JSON 兼容的版本。
    """
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[item_id] = json_compatible_item_data
