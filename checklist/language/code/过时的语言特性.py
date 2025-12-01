
# 字符串对象的方法来取代string模块中的函数
text = " hello "
print(text.strip()) # 去掉左右的空格
print(text.split(',')) # 按照逗号分隔
# 替代
import string
print(string.strip(text))

# 替代apply()方法
def eg_func(a,b,c):
    print(a,b,c)

args=(1,2,3)
eg_func(*args) #解包调用

# 不推荐
# apply(eg_func,args)

# 使用for循环/列表推导式 替代filter map reduce,提高可读性
nums=[1,2,3,4,5]
filtered = [x for x in nums if x%2==0]
# map:
squared = list(map(lambda x:x**2 ,nums))

# 使用列表推导式代替map:得到迭代器
squared=[x**2 for x in nums]

from functools import reduce 
result=reduce(lambda x,y:x*y ,nums)
