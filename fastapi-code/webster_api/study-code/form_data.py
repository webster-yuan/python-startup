# 当需要接收表单字段而不是JSON时,可以使用Form

from typing import Annotated
from fastapi import FastAPI, Form

app = FastAPI()

# 在 OAuth2 规范的一种使用方式（称为“密码流程”）中，需要发送 username 和 password 作为表单字段。
# 该 规范 要求字段的名称必须是 username 和 password，并且必须作为表单字段发送，而不是 JSON。
# 使用 Form，你可以声明与 Body（以及 Query、Path、Cookie）相同的配置，包括验证、示例、别名（例如 user-name 而不是 username）等
@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}

# 表单字段
# HTML 表单（<form></form>）发送数据到服务器的方式通常使用“特殊”编码来对该数据进行编码，它与 JSON 不同。
# FastAPI 将确保从正确的位置读取数据，而不是 JSON。