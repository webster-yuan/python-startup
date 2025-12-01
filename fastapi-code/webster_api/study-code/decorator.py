import fastapi


# 装饰器
def my_decorator(func):
    def wrapper():
        print("before call func")
        func()
        print("after call func")

    return wrapper


@my_decorator
def say_hello():
    print("hello")


say_hello()


# 带参数的装饰器
def my_decorator_1(func):
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result

    return wrapper


@my_decorator_1
def say(message):
    print(message)


say("hello with a message")

# fastapi中应用
# @webster_api.get("/") 和 @webster_api.post("/items/") 是 FastAPI 装饰器，它们将函数绑定到特定的 HTTP 方法和路径上。当 HTTP 请求到达这些路径时，
# 相应的函数将被调用，并处理这些请求。
app = fastapi.FastAPI()


@app.get("/")
async def read_root():
    return {"hello": "world"}


@app.post("/items")
async def create():
    return "str"
