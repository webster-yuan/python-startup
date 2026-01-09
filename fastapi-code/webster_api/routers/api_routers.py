from fastapi import APIRouter

from .routers import hero_router

api_router = APIRouter()

api_router.include_router(hero_router)
