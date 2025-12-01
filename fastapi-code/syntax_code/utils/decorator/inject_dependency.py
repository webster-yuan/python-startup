from functools import wraps


def inject_dependency(**dependencies):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            new_kwargs = {**dependencies,**kwargs }
            return func(*args, **new_kwargs)
        return wrapper
    return decorator

@inject_dependency(database="mysql")
def connect_database(database, **kwargs):
    print(f"Connect to {database}, extra args: {kwargs}")

if __name__ == '__main__':
    connect_database()  #Connect to mysql
    connect_database(database="666")
#     既然是依赖注入，为什么不刻意这样
    connect_database(name="666")
    # 我想最后一个默认打印database="666" database="mysql"，这才算把传进来的key-value和默认的整合到一起


