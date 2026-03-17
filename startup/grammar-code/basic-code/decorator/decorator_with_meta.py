# 默认装饰器会覆盖原函数的元信息（如 __name__、文档字符串），需用 functools.wraps 修复。
# 生产环境必须加 @wraps(func)，否则原函数的 __name__、__doc__、参数签名会丢失；
# 不影响参数传递逻辑，仅修复元信息。

import time
from functools import wraps

def timer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"函数 {func.__name__} 执行耗时：{time.time() - start_time:.4f} 秒")
        return result
    
    return wrapper

@timer_decorator
def calculate_sum(num_list, multiplier=1):
    """
    计算列表元素的和，并乘以乘数
    :param num_list: 数字列表
    :param multiplier: 乘数（默认1）
    :return: 求和结果
    """
    time.sleep(0.05)
    return sum(num_list) * multiplier

# 调用测试
print(calculate_sum([1,2,3,4], multiplier=2))  # 输出：函数 calculate_sum 执行耗时：0.0501 秒 → 20

# 验证元信息（未用 wraps 时，__name__ 会变成 wrapper，文档字符串丢失）
print(calculate_sum.__name__)  # 输出：calculate_sum（正确）
print(calculate_sum.__doc__)   # 输出：函数的文档字符串（正确）