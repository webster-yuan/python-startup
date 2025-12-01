# 获取当前日期和时间并计算日期差
from datetime import datetime,timedelta

now =datetime.now()
print("当前日期和时间:",now)
# 计算7天之后的日期
future_time = now + timedelta(days=7)
print("7天之后的日期:",future_time)

# 计算两个日期之间的差值
past_date = datetime(2024,1,1)
date_diff = now - past_date
print(f"两个日期之间的差值:{date_diff.days}天")