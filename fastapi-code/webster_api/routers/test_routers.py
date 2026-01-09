from fastapi import APIRouter

from .demo_routers.path_param import path_param_router
from .demo_routers.query_param import query_param_router
from .demo_routers.req_body import req_body_router
from .demo_routers.other_data_type import other_data_type_router
from .demo_routers.header_cookie import header_cookie_router
from .demo_routers.header import header_router
from .demo_routers.exception_demo import exception_router
from .demo_routers.depends import depends_router

test_router = APIRouter()

test_router.include_router(path_param_router)
test_router.include_router(query_param_router)
test_router.include_router(req_body_router)
test_router.include_router(other_data_type_router)
test_router.include_router(header_cookie_router)
test_router.include_router(header_router)
test_router.include_router(exception_router)
test_router.include_router(depends_router)
