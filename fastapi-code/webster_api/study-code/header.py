from fastapi import FastAPI, Header
from typing import Union, Annotated, List

app = FastAPI()


# 大多数标准头部用“连字符”字符（也称为“减号”（-））分隔。
# 像 user-agent 这样的变量在 Python 中是无效的,所以
# 默认情况下，Header 会将参数名称字符从下划线（_）转换为连字符（-）以提取和记录头部
# 所以=> 不用担心变量中的下划线，**FastAPI** 会负责将它们转换
@app.get("/items/")
async def read_items(user_agent: Annotated[Union[str, None], Header()] = None):
    return {"User-Agent": user_agent}


# 如果出于某种原因您需要禁用将下划线自动转换为连字符，
# 请将 Header 的参数 convert_underscores 设置为 False
@app.get("/items/")
async def read_items(
    strange_header: Annotated[
        Union[str, None], Header(convert_underscores=False)
    ] = None
):
    return {"User-Agent": strange_header}
# 在将 convert_underscores 设置为 False 之前，
# 请记住，某些 HTTP 代理和服务器不允许使用带下划线的头部。


# 2. 重复头部:一个头部有多个值
@app.get("/items")
async def read_items2(x_token: Annotated[Union[List[str], None], Header()] = None):
    return {"X-Token values": x_token}
# 如果您与该路径操作通信，发送两个像这样的 HTTP 头部
# X-Token: foo
# X-Token: bar
# 响应:
# {
#     "X-Token values": [
#         "bar",
#         "foo"
#     ]
# }