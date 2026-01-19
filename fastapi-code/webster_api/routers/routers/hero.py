from fastapi import APIRouter, Query, Depends
from typing import Annotated

from webster_api.db.sqlite import SessionDep
from webster_api.core.deps import get_current_active_user
from webster_api.schemas.hero import HeroCreate, HeroRead
from webster_api.services.hero import delete_hero_service, create_hero_service, select_heros, select_heros_service, \
    select_hero_by_id_service

hero_router = APIRouter(
    prefix="/hero",
    tags=["hero"],
    # All hero endpoints require authentication
    dependencies=[Depends(get_current_active_user)],
)


@hero_router.post("/hero")
async def create_hero(hero: HeroCreate, session: SessionDep) -> int:
    return create_hero_service(session, hero)


@hero_router.get("/heros", response_model=list[HeroRead])
async def read_heros(
        session: SessionDep,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
):
    return select_heros_service(session, offset=offset, limit=limit)


@hero_router.get("/hero/{query_id}", response_model=HeroRead)
async def read_hero(
        session: SessionDep,
        query_id: int,
):
    return select_hero_by_id_service(session, query_id)


@hero_router.delete("/hero/{delete_id}")
async def delete_hero(session: SessionDep, delete_id: int):
    """
    1. 拿参数
    2. 调 service
    3. 返回 HTTP 响应
    """
    delete_hero_service(session, delete_id)
    return {"ok": True}
