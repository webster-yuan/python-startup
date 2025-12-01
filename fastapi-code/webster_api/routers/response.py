from fastapi import APIRouter, Response

response_router = APIRouter(prefix="/item", tags=["item"])


@response_router.get("/headers-and-object/")
def get_headers(response: Response):
    response.headers["webster"] = "webster_token"
    return "hello webster_api"
