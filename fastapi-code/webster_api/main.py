# webster_api/main.py
from fastapi import FastAPI
import uvicorn
from routers import item_router, response_router

app = FastAPI()

app.include_router(item_router)
app.include_router(response_router)


# 打印已经注册的路由有哪些
@app.on_event("startup")
async def startup_event():
    for route in app.routes:
        print(f"Path: {getattr(route, 'path', None)}, Methods: {getattr(route, 'methods', None)}")


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
