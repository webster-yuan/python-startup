import time

# 定义无参数装饰器（统计函数执行时间）
def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 执行耗时: {end_time - start_time:.4f}")
        return result
    
    return wrapper

@time_decorator
def add(a, b , c =0):
    time.sleep(1)

    return a+b+c