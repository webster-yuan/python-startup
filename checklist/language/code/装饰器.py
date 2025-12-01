

def timing_decorator(func):
    """装饰器:记录函数运行时间"""
    # 写在函数内部,减少全局依赖
    import time
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result = func(*args,**kwargs)
        end_time=time.time()
        print(f"{func.__name__} executed in {end_time-start_time:.2f}s")
        return result
    return wrapper

@timing_decorator
def eg_func(n):
    for _ in range(n):
        pass
eg_func(1000000000000)


def logger_decorator(log_func):
    """装饰器:日志记录功能,不依赖外部文件"""
    def wrapper(func):
        def wrapped(*args,**kwargs):
            log_func(f"Calling {func.__name__}")
            return func(*args,**kwargs)
        return wrapped
    return wrapper

# 简单日志函数,避免文件依赖
def simple_logger(message):
    print(f"log:{message}")
    
@logger_decorator(simple_logger)
def samle_func():
    print("Function executed")
samle_func()

