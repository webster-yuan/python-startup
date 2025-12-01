from functools import wraps


def cache(func):
    calculate_list = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args in calculate_list:
            print(f"Cache hit for {args}")
            return calculate_list[args]
        result = func(*args)
        calculate_list[args] = result
        return result
    return wrapper

@cache
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-2)+fibonacci(n-1)

if __name__ == '__main__':
    print(fibonacci(10))  # 第一次计算，无缓存
    print(fibonacci(10))  # 直接返回缓存结果

# Cache hit for (1,)
# Cache hit for (2,)
# Cache hit for (3,)
# Cache hit for (4,)
# Cache hit for (5,)
# Cache hit for (6,)
# Cache hit for (7,)
# Cache hit for (8,)
# 55
# Cache hit for (10,)
# 55

# @wraps 是 functools.wraps 的装饰器工厂函数，必须接收一个参数（即被装饰的原始函数 func），
# 才能将原始函数的元数据复制到装饰后的 wrapper 函数中。如果代码中未传递 func，导致以下问题：
#
# 元数据丢失：wrapper 函数没有继承 fibonacci 的元数据（如 __name__、__doc__ 等）。
#
# 递归调用失效：当 fibonacci 第一次被调用的时候，触发装饰机制，代码外面被wrapper函数代码封装为 fibonacci_plus ，
# 以后每次调用都是 fibonacci_plus，递归调用自身时，实际调用的是 wrapper（fibonacci_plus） 函数。
# 如果 wrapper 的元数据不正确，递归可能会错误地引用到其他对象（比如错误地引用了一个 int 类型），从而触发 AttributeError。