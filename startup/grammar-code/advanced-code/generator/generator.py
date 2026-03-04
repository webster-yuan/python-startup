# 生成器: 简化版本的迭代器
# 不用动手实现__iter__()和__next__(),用yield关键字就能创建
# 是Python中最常用的迭代器实现方式

# 生成器函数
# 函数体包含yield关键字,调用函数不执行函数体,而是返回生成器对象
# yield 会暂停函数执行,next()会回复执行并返回yield后的值

# 示例1: 基础生成器函数
from collections.abc import Iterator
def my_range(n):
    current = 0
    while current<n:
        current+=1
        yield current # 暂停执行，返回current；下次next()从这里继续

# 调用函数,得到生成器对象
gen = my_range(3)
print(isinstance(gen, Iterator))

print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))
# 1
# 2
# 3
# Traceback (most recent call last):
#   File "E:\code\python-startup\startup\grammar-code\advanced-code\generator\generator.py", line 23, in <module>
#     print(next(gen))
# StopIteration

# 示例2:生成器的暂停-恢复特性
def demo_generator():
    print("first step")
    yield 1
    print("second step")
    yield 2
    print("third step")
    yield 3

gen = demo_generator()
next(gen)
# next(gen)
# next(gen)

# first step

# 生成器表达式
# 类似于列表推导式，把[]换成()
# 惰性计算，内存占用极低（对比列表推到式）
list1 = [x*2 for x in range(1000)]
print(type(list1))

gen1 = (x*2 for x in range(1000))
print(type(gen1))
print(next(gen1))
print(next(gen1))
# <class 'list'>
# <class 'generator'>
# 0
# 2

# 生成器核心优势: 节省内存,当处理大数据时
# 问题: 遍历1000万条数据,计算偶数和
# wrong: 使用列表会占用大量内存,可能卡顿
# right: 使用生成器,几乎不占内存

def get_even_gen(n):
    for i in range(n):
        if i%2==0:
            yield i

custom_sum = 0
even_gen = get_even_gen(10000000)
for num in even_gen:
    custom_sum+=num

print(custom_sum) # 24999995000000

# 生成器进阶用法: 接收外部send()传值传入的值
def counter():
    count =0 
    while True:
        inc = yield count
        if inc is None:
            inc = 1
        
        count+=inc

gen2 = counter()
print(next(gen2))
print(gen2.send(2))
print(gen2.send(3))
print(next(gen2))
# 0
# 2
# 5
# 6

# 用途: 读取大文件:逐行读取G级日志文件,避免一次性加载到内存
# def read_big_file(file_path):
#     with open(file_path, "r", encoding="utf-8") as f:
#         for line in f:
#             yield line.strip()

# # 使用: 遍历大文件,处理每一行
# for line in read_big_file("big_log.txt"):
#     if "error" in line:
#         print(line)

# 无限序列生成
def fibonacci():
    a, b =0,1
    while True:
        yield a
        a, b = b ,a+b

# 取前10个斐波那契数
fib_gen = fibonacci()
for _ in range(10):
    print(next(fib_gen))
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34