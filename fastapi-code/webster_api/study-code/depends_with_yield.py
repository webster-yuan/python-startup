# fastapi支持在完成某些额外的步骤后的依赖项,使用yield不是return

# 带有yield的数据库依赖项
# async def get_db():
#     db=DBSession()
#     try:
#         yield db 调用该依赖项时抛出的任何异常
#     finally:
#         db.close()

# 带有yield的子依赖项
from typing import Annotated
from fastapi import Depends


async def dependency_a():
    dep_a = generate_dep_a()
    try:
        yield dep_a
    finally:
        dep_a.close()


async def dependency_b(dep_a: Annotated[DepA, Depends(dependency_a)]):
    dep_b = generate_dep_b()
    try:
        yield dep_b
    finally:
        dep_b.close(dep_a)


async def dependency_c(dep_b: Annotated[DepB, Depends(dependency_b)]):
    dep_c = generate_dep_c()
    try:
        yield dep_c
    finally:
        dep_c.close(dep_b)  # dep_c退出代码时要保证dep_b是可用的,同理...


from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

data = {
    "plumbus": {"description": "Freshly pickled plumbus", "owner": "Morty"},
    "portal-gun": {"description": "Gun to create portals", "owner": "Rick"},
}

# 带有yield和HTTPException的依赖项
class OwnerError(Exception):
    pass


def get_user_name():
    try:
        yield "Rick"
    except OwnerError as e:
        raise HTTPException(status_code=400, detail=f"Owner error: {e}")


@app.get("/items/{item_id}")
def get_item(item_id: str, username: Annotated[str, Depends(get_user_name)]):
    if item_id not in data:
        raise HTTPException(status_code=404, detail="item not found")
    item = data[item_id]
    if item["owner"] != username:
        raise OwnerError(username)
    return item

# 带有yield和except的依赖项
# 没有再次抛出异常,fastapi无法注意到异常,客户端会看到HTTP500,但是
# 服务器没有任何体质或者其他只是错误原因的信息
def get_username():
    try:
        yield "Rick"
    except InternalError:
        print("Oops, we didn't raise again, Britney 😱")
        
# 在带有 yield 和 except 的依赖项中始终 raise
# 这样客户端会收到500,服务器将有我们自定义的InternalError在日志中
def get_username():
    try:
        yield "Rick"
    except InternalError:
        print("We don't swallow the internal error here, we raise again 😎")
        raise
    
# 上下文管理器 是可以用在with语句中的任何python对象

class MySuperContextManager:
    def __init__(self) -> None:
        self.db=DBSession()
    
    def __enter__(self):
        return self.db
    
    def exit(self,exc_type,exc_value,traceback):
        self.db.close()

async def get_db():
    with MySuperContextManager as db:
        yield db