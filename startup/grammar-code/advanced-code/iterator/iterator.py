# Python 中的迭代器(Iterator) 和生成器(Generator)是处理大规模数据,延迟计算和高效内存管理的重要工具.
# 他们允许我们逐个生成元素,而不是一次性加载所有数据,从而大幅减少内存损耗.


# 一. 可迭代对象: 能够被for循环遍历的对象(列表,字符串,字典,元组等)
# 本质是实现了__iter__()方法的对象
# 验证: 用 isinstance() 检查是否是可迭代对象

# 1. 常见可迭代对象
from collections.abc import Iterable, Iterator
list1 = [1,2,3]
string1 = "hello"
dict1 = {"a":1 , "b":2}

print(isinstance(list1, Iterable))
print(isinstance(string1, Iterable))
print(isinstance(dict1, Iterable))

# True
# True
# True

# 2. for循环的本质,调用可迭代对象的__iter__()得到迭代器,再遍历迭代器
# 手动模拟for循环的过程
iter_list = list1.__iter__() #等价于iter(lst)
print(isinstance(iter_list, Iterator))
# True

# 二. 迭代器: 可迭代对象的遍历工具
# 是一种惰性计算的对象(用到的时候才生成下一个值)
# 必须实现两个方法
# __iter__():返回迭代器自身,保证迭代器也是可迭代对象
# __next__():返回下一个元素,遍历完抛StopIteration异常
# 特点: 只能往前遍历,不能回退;遍历一次就耗尽(不可逆)

# 1. 创建迭代器
list2 = [1,2,3]
iter_list2 = iter(list2)# 等价于 lst.__iter__()

print(isinstance(iter_list2, Iterator))
# True

# 2. 用__next__()遍历（手动调用）
print(next(iter_list2))
print(next(iter_list2))
print(next(iter_list2))
# print(next(iter_list2))

# 1
# 2
# 3
# Traceback (most recent call last):
#   File "E:\code\python-startup\startup\grammar-code\advanced-code\iterator\iterator.py", line 47, in <module>
#     print(next(iter_list2))
# StopIteration
for num in list2:
    print(num)

# 3. 自定义迭代器
class MyRangeIterator:
    def __init__(self, n:int):
        self.n = n
        self.current = 0 # 记录当前位置
    
    # 迭代器必须实现__iter__,返回自身
    def __iter__(self):
        return self
    
    # 核心:实现__next__,返回下一个值
    def __next__(self):
        self.current+=1
        if self.current<=self.n:
            return self.current
        else:
            raise StopIteration
        
custom_iterator = MyRangeIterator(3)
for num in custom_iterator:
    print(num)
