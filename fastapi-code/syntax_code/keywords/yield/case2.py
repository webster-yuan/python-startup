# 无限循环中的yield

def infinite_counter():
    count = 0
    while True:
        yield count
        count += 1


if __name__ == '__main__':
    gen = infinite_counter() # 生成器对象
    print(next(gen))
    print(next(gen))
    # 0
    # 1