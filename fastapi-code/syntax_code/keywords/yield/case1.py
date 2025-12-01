# 生成器函数中的循环会逐次执行，每次遇到 yield 时暂停并返回一个值。
# 下一次调用 next() 或触发迭代时，
# 生成器会从 yield 的下一条语句恢复执行，直到循环结束或遇到下一个 yield。


def loop_yield(n):
    for i in range(n):
        yield f"第{i}次产出"


if __name__ == '__main__':
    gen = loop_yield(3)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    # 第0次产出
    # 第1次产出
    # 第2次产出
    # Traceback (most recent call last):
    #   File "G:\startup\fastapi-code\syntax_code\keywords\yield\case1.py", line 16, in <module>
    #     print(next(gen))
    #           ~~~~^^^^^
    # StopIteration
