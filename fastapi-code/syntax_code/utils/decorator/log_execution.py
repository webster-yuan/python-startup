import time
from functools import wraps


def log_execution(func):
    @wraps(func)  # @wraps(func) 的作用是让 装饰后的函数（wrapper）伪装成原始函数（cal_sum），避免元数据被覆盖。
    def wrapper(*args, **kwargs): # wrapper ：包装纸
        state_time = time.time()
        print(f"func: {func.__name__} Start executing with  args:{args},"
              f"kwargs:{kwargs}")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Finished {func.__name__} in {end_time - state_time:.4f}s, "
              f"Func execute Result:{result}")
    return wrapper


@log_execution
def cal_sum(a:int, b:int):
    time.sleep(5)
    return a+b


if __name__ == '__main__':
    cal_sum(10,20)
    print("Function name (with @wraps):", cal_sum.__name__)
    print("Function docstring (with @wraps):", cal_sum.__doc__)


# 将 @wraps(func) 注释
# func: cal_sum Start executing with  args:(10, 20),kwargs:{}
# Finished cal_sum in 5.0008s, Func execute Result:30
# Function name (with @wraps): wrapper
# Function docstring (with @wraps): None

# 保留 @wraps(func)
# func: cal_sum Start executing with  args:(10, 20),kwargs:{}
# Finished cal_sum in 5.0009s, Func execute Result:30
# Function name (with @wraps): cal_sum
# Function docstring (with @wraps): None