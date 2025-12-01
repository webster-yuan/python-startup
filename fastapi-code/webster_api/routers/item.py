from fastapi import APIRouter

item_router = APIRouter(prefix="/item", tags=["item"])


@item_router.get("/items/")
async def read_items():
    return [{"item_id": "Foo"}]
