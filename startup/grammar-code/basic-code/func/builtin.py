# 1. abs 返回绝对值
print(abs(-123))
# 2. sum 需要放可迭代对象（字符串是但是不行，列表，集合,元组）
print(sum((1,2)))
# 只要有一个浮点数参与运算，结果就是浮点数
print(sum([1.5,2,3]))
#6.5

# 3. min
print(min(4,1,2))
print(min(-4,1,2,key=abs))# 求绝对值的最小值
# 4. max
print(max(5,3,2))

# 5. zip:将可迭代对象作为参数，将对应的元素打包为一个个元组
list1 = [1,2,3]
list2 = ['a','b','c']
print(type(zip(list1, list2)))
for i in zip(list1, list2):
    print(i)

# <class 'zip'>
# (1, 'a')
# (2, 'b')
# (3, 'c')

# 元素个数不一致时，按照最短的返回
list3=['A','B']
for i in zip(list1, list3):
    print(i)

# (1, 'A')
# (2, 'B')

# 转换为列表打印
print(list(zip(list1,list3)))
# [(1, 'A'), (2, 'B')]

# 6. map： 可以对可迭代对象中的每一个元素进行映射，分别去执行
# map(func, iter1): func自己定义的函数，iter1要放进去的可迭代对象
# 让可迭代对象中的每一个元素都去执行func
list4 = [1,2,3]
def func(x):
    return x*5

mp = map(func, list4)
# for m in mp:
#     print(m)
#     # 5
#     # 10
#     # 15

print(list(mp))
# [5, 10, 15]

# 7. reduce: 先把对象中的两个元素取出来，计算出一个值，然后保存，接下来把这个值和第三个元素进行计算
# 需要先导包
from functools import reduce
# reduce(function, sequence) function: 必须是有两个参数的函数 sequence：序列，可迭代对象
add = lambda x, y :x+y
list5= [1,2,3]
res = reduce(add, list5)
print(res)
# 6

# 8. 拆包：对于函数中的多个返回数据，去掉元组，列表，或者字典，直接得到里面的数据
tup = (1,2,3,4)
print(type(tup), tup)
# <class 'tuple'> (1, 2, 3, 4)
print(tup[2])
# 方法一：变量赋值：变量个数与元组内的元素个数相同
a,b,c,d = tup
print(f"a:{a},b:{b},c:{c},d:{d}")
# a:1,b:2,c:3,d:4

# 方法二：* 将剩下的都交给*的变量承接
e, *f = tup
print(f"e:{e},f:{f}, type(f):{type(f)}")
# e:1,f:[2, 3, 4], type(f):<class 'list'>