import time

# 定义带参装饰器（可指定超时提示文案）

# 为了给装饰器传参的「函数嵌套」
def timeout_decorator(timeout_msg="函数执行时"): # 外层：收装饰器参数
    def decorator(func):                        # 中层：收被装饰函数
        def wrapper(*args, **kwargs):           # 内层：执行逻辑
            print(f"元组第一个元素,args[0]:{args[0]}")

            start_time = time.time()
            result = func(*args, **kwargs)
            cost_time = time.time() - start_time

            limit  = kwargs.get("limit")
            if limit and cost_time > limit:
                print(f"{timeout_msg}：{func.__name__} 耗时 {cost_time:.4f} 秒")

            return result
        
        return wrapper
    
    return decorator

# 装饰带参数的函数（装饰器传自定义参数）
@timeout_decorator(timeout_msg="【警告】加法函数执行超时")
def add(a, b, c=0):
    time.sleep(0.15)  # 模拟超时
    return a + b + c

print(add(10, 20, limit=30))    # 输出：【警告】加法函数执行超时：add 耗时 0.1501 秒 → 60


@timeout_decorator()  # 装饰器参数用默认值
def multiply(x, y):
    time.sleep(0.08)  # 未超时
    return x * y

# 调用测试
print(multiply(5, 6))       # 无超时提示，输出 30