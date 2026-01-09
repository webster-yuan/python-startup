from fastapi import HTTPException
from fastapi import APIRouter

from webster_api.exception import BusinessException

exception_router = APIRouter(prefix="/exception", tags=["exception"])
items = {"foo": "The Foo Wrestlers"}


@exception_router.get("../exception/items")
async def exception_item_get(item_id: str):
    if item_id not in items:
        # Python 异常
        raise HTTPException(status_code=404,
                            detail="Item not found",
                            headers={"X-Error": "There goes my error"},
                            )

    return items[item_id]


# 自定义异常
@exception_router.get("/test")
async def test_exception():
    raise BusinessException("Rainbow Dash")
