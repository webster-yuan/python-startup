from fastapi import Request
from fastapi.responses import JSONResponse


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


async def unicorn_exception_handler(
        request: Request,
        exc: UnicornException,
):
    return JSONResponse(
        status_code=418,
        content={
            "error": "UnicornException",
            "name": exc.name,
            "path": request.url.path,
        }
    )
