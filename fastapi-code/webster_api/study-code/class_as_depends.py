from typing import Annotated, Union, Any

from fastapi import FastAPI, Depends

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# 在fastapi中,Python类也是一个可调用对象,用作依赖项
# fastapi实际上检查的是它是否是一个可调用对象(函数,类)以及参数
# 将可调用对象作为依赖项传递,将分析它的参数,以与路径操作函数的参数相同的方式处理他们


# 将函数->类
# __init__ 函数与common_parameters具有相同的参数
class CommonQueryParams:
    def __init__(self, q: Union[str, None] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


# 使用类来声明依赖项,会创建一个该类的实例,并将实例作为参数commons传递给函数
@app.get("/items/")
async def read_items_v1(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response


# 类型注释与Depends
# Depends()中识别依赖项类
# Annotated[CommonQueryParams...
# 第一个参数类型没有任何意义,fastapi不会对它进行数据转换验证等
@app.get("/items/")
async def read_items_v2(commons: Annotated[Any, Depends(CommonQueryParams)]):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response


# 但是还是建议写上,是为了让编辑器知道并帮助你进行代码补全,类型检查
@app.get("/items/")
async def read_items_v3(commons:CommonQueryParams=Depends(CommonQueryParams)):
    response={}
    if commons.q:
        response.update({"q":commons.q})
    items=fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items":items})
    return response


# 为了避免重复书写CommonQueryParams,fastapi针对这种情况提供一个快捷方式
# 只用写第一个类型即可,在Depends中不用声明依赖项(可调用对象(函数,类))
@app.get("/items/")
async def read_items_v4(commons: Annotated[CommonQueryParams, Depends()]):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response