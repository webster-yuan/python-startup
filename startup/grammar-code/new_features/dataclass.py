# 3.7 的 dataclasses，能自动生成__init__、repr，定义数据模型时省很多代码

from dataclasses import dataclass

# 装饰器
@dataclass
class User:
    name:str
    age:int

user = User("Alice", 30)
print(user) # User(name='Alice', age=30)


# 如果没有使用 dataclass 装饰器，
# 需要自己实现__repr__，否则输出会是 <__main__.User object at 0x...>
