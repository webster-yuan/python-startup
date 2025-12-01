import time
from functools import wraps

# 统计函数执行时间，用于性能优化

# 性能分析装饰器
def profile(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() -start
        print(f"func {func.__name__} executed in {elapsed:.6f} seconds")
        return result
    return wrapper

@profile
def heavy_computation(n):
    return sum(i*i for i in range(n))

if __name__ == '__main__':
    heavy_computation(10*6)
# func heavy_computation executed in 0.000012 seconds