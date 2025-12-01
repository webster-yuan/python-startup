from datetime import datetime
from typing import Union

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

fake_db={}

class Item(BaseModel):
    title:str
    timestamp:datetime
    description:Union[str,None]=None

app =FastAPI()

@app.put("/items/{id}")
def update_item(id:str,item:Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id]=json_compatible_item_data

# 在此示例中，它会将 Pydantic 模型转换为 dict，并将 datetime 转换为 str。

# 调用它的结果是可以使用 Python 标准 json.dumps() 进行编码的东西。

# 它不会返回一个包含 JSON 格式数据的字符串 (作为字符串) 的大型 str。
# 它返回一个 Python 标准数据结构 (例如 dict)，其值和子值都与 JSON 兼容
# 与 JSON 兼容的原生数据结构 的意思是，这些数据结构是 Python 的原生类型，比如 dict、list、str、int 等，但它们的格式和数据类型可以直接被 JSON 编码器（如 json.dumps()）序列化为 JSON 格式的字符串。
# 没有转换为 JSON 格式字符串：jsonable_encoder 生成的结果仍然是 Python 的标准数据结构（比如 dict），而不是 JSON 格式的字符串。也就是说，它的输出可以直接用于后续操作，如存储、传输、处理，但它不是一个 JSON 字符串（即它不是直接可以发送给客户端的 HTTP 响应体）