import time
from functools import wraps


# 此次给装饰器传递了参数
# 使用示例
def retry(max_retries: int = 5, delay: int = 1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed :{e}")
                    time.sleep(delay)
            raise Exception("All retries exhausted")

        return wrapper

    return decorator


@retry(max_retries=2, delay=2)
def connect_to_database():
    print("Connecting to database...")
    raise ConnectionError("Database unreachable")


if __name__ == '__main__':
    connect_to_database()

# Connecting to database...
# Attempt 1 failed :Database unreachable
# Connecting to database...
# Attempt 2 failed :Database unreachable
# Traceback (most recent call last):
#   File "G:\startup\fastapi-code\syntax_code\utils\decorator\retry.py", line 25, in <module>
#     connect_to_database()
#     ~~~~~~~~~~~~~~~~~~~^^
#   File "G:\startup\fastapi-code\syntax_code\utils\decorator\retry.py", line 15, in wrapper
#     raise Exception("All retries exhausted")
# Exception: All retries exhausted
