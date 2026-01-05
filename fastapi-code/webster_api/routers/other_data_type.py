from http.client import HTTPException
from uuid import UUID

from fastapi import APIRouter, Body
from typing import Annotated
from datetime import datetime, timedelta, time

other_data_type_router = APIRouter(prefix="/other-data", tags=["other-data"])


@other_data_type_router.get("/items")
async def other_data_type_get_items(
        item_id: UUID,
        start_time: Annotated[datetime, Body()],
        end_time: Annotated[datetime, Body()],
        process_after: Annotated[timedelta, Body()],
        repeat_at: Annotated[time, Body()],
):
    # start_time: 用户希望开始时间
    # process_after: 接口层把“延迟启动”这一业务规则暴露并落地了
    # end_time： 用户希望结束时间
    start_process = start_time + process_after
    duration = end_time - start_process
    if duration <= timedelta(0):
        raise HTTPException(422, "end_datetime 必须大于 start_datetime + process_after")

    return {
        "item_id": item_id,
        "start_datetime": start_time,
        "end_datetime": end_time,
        "process_after": process_after,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }
    # {
    #   "start_time": "2026-01-05T15:21:48.833Z",
    #   "end_time": "2026-01-05T15:21:48.833Z",
    #   "process_after": "P3D",
    #   Period 3 Days 3 天
    #   PT6H	6 小时
    #   PT30M	30 分钟
    #   P1DT2H3M4S	1 天 2 时 3 分 4 秒
    #   P1W	1 周（7 天）
    #   "repeat_at": "15:21:48.833Z"
    # }
