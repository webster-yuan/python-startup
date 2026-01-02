import time
from functools import lru_cache


# 自动记忆化，重复计算秒消失,常用于递归,存在重复计算的情况,命中缓存

@lru_cache(maxsize=None)  # 无上限缓存
def fib(n):
    return n if n < 2 else (fib(n - 1) + fib(n - 2))


if __name__ == '__main__':
    start = time.perf_counter()
    ret = fib(35)  # 9227465
    print(f"fib 35 is {ret}, cost time is : {time.perf_counter() - start}")
    # 第二次 fib(35) 直接读缓存，≈ 0 s
