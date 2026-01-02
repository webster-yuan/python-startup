# @contextmanager 生成器版（推荐）
# 将一个生成器函数快速转换为上下文管理器
# 无需手动定义实现 __enter__() __exit__() 方法的类,简化上下文管理器代码编写

# 被@contextmanager装饰的生成器函数必须遵循 “前操作 → yield → 后操作” 的三段式结构
# 1. yield之前的代码：对应上下文管理器的__enter__()方法，进入with代码块时执行；
# 2. yield语句：作为上下文的 “分隔点”，暂停生成器，执行with代码块内的业务逻辑；若yield后带值，可通过with ... as var接收该值；
# 3. yield之后的代码：对应上下文管理器的__exit__()方法，退出with代码块时（无论正常结束还是异常报错）执行，负责收尾工作。

# 多个上下文管理器逗号串联的规则：
# with A(), B(): 等价于嵌套的with A(): with B():，执行顺序为：
# 进入时：先执行A的__enter__()（即A生成器yield前代码），再执行B的__enter__()（即B生成器yield前代码）；
# 执行with代码块内逻辑；
# 退出时：先执行B的__exit__()（即B生成器yield后代码），再执行A的__exit__()（即A生成器yield后代码）（先进后出，类似栈结构
from contextlib import contextmanager
import time


@contextmanager
def tag(name):
    print(f'<{name}>')
    yield
    print(f'</{name}>')


@contextmanager
def timer():
    start = time.perf_counter()
    yield
    print(f'[timer] cost {time.perf_counter() - start:.3f}s')


if __name__ == '__main__':
    with tag('html'), timer():
        time.sleep(1)

# <html>
# [timer] cost 1.010s
# </html>
