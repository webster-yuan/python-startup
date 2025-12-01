from functools import wraps

def file_decorator(file_name, mode):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(file_name, mode) as file:  # ✅ 在 wrapper 中管理文件
                return func(file, *args, **kwargs)
        return wrapper
    return decorator

@file_decorator("data.txt", "w")
def write_file(file):
    file.write("hello world")

write_file()  # 调用时自动打开/关闭文件


# 使用 with 语句（推荐），上下文管理器+yield
from contextlib import contextmanager

@contextmanager
def file_manager(file_name, mode):
    file = open(file_name, mode)
    try:
        yield file
    finally:
        file.close()

# 通过 with 调用
with file_manager("data.txt", "w") as file:
    file.write("hello world")