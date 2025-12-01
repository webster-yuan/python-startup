# 可以创建具有子依赖项的依赖项,可以根据需要深入处理
from typing import Annotated, Union
from fastapi import FastAPI, Depends, Cookie

app = FastAPI()


# 第一个依赖项dependable
def query_extractor(q: Union[str, None] = None):
    return q

# dependant
def query_or_cookie_extractor(
    q: Annotated[str, Depends(query_extractor)],
    last_query: Annotated[Union[str, None], Cookie()] = None,
):
    if not q:
        return last_query
    return q


@app.get("/items/")
async def read_query(
    query_or_default: Annotated[str, Depends(query_or_cookie_extractor)],
):
    return {"q_or_cookie": query_or_default}

# 第二个依赖项,dependable(可以被依赖的资源) dependant(正在依赖其他资源,函数)

# 当多次使用相同的依赖项时,也就是多个依赖项调用 query_or_cookie_extractor,
# 或者一个依赖项的多个步骤多次调用 query_or_cookie_extractor
# fastapi会做出优化,将这个 dependable放到cache缓存中,
# 如果你就就是想每次都调用获取最新的值,而不是缓存值
def get_value():
    pass

@app.get("/items/")
async def needy_dependency(fresh_value:Annotated[str,Depends(get_value,use_cache=False)]):
    return {"fresh_value":fresh_value}