# 生成器和装饰器

def count_up_to(max):
    count = 1
    while(count <= max):
        yield count
        # yield作用: 产出一个值，并暂停函数的执行，下一次调用函数时从上次暂停的地方继续执行
        count += 1

counter = count_up_to(5)
for num in counter:
    print(num)