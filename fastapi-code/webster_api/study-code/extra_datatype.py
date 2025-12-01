
from datetime import datetime,time,timedelta
from fastapi import FastAPI, Body
from typing import Annotated,Union
from uuid import UUID

app = FastAPI()

# datetime 是用来处理具体的日期和时间点的。
# date 是截止到日期
# time 更关注于一天之内的具体时间。
# timedelta 用于表示时间间隔，并且常常用于日期时间的计算。

@app.put("/items/{item_id}")
async def read_items(
    item_id:UUID,
    start_datetime:Annotated[datetime,Body()],
    end_datetime:Annotated[datetime,Body()],
    process_after:Annotated[timedelta,Body()],
    repeat_at:Annotated[Union[time,None],Body()]=None,
):
    start_process =start_datetime+process_after
    duration=end_datetime-start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_after,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }