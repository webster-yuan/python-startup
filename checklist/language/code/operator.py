import operator

# operator.mul  map??
list1 = [1,3,2]
list2 = [4,5,6]
result = list(map(operator.mul,list1,list2))
# 替代lambda
result=list(map(lambda x,y: x*y,list1,list2))

# 与functools.reduce,计算序列乘积 reduce??
from functools import reduce

numbers=[1,2,3,4]
result=reduce(operator.mul,numbers)
print(result)

# 等价于lambda
result=reduce(lambda x,y:x*y,numbers)

# 矩阵按元素相乘 zip??
matrix1=[[1,2],[3,4]]
matrix2=[[2,0],[1,5]]

result=[[operator.mul(a,b) for a,b in zip(row1,row2)] for row1,row2 in zip(matrix1,matrix2)]
print(result)


# map:用于将计算后的结果生成一个迭代器
# 两个列表逐项相加
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = map(lambda x, y: x + y, list1, list2)
print(list(result))  # 输出 [5, 7, 9]

# reduce:用于将可迭代对象的元素通过二元函数累计计算
# 最终得到一个值
nums = [1,2,3,4]
result = reduce(lambda x,y:x*y,numbers)
print(result) # 24
# 带初始值的计算
result=reduce(lambda x,y:x*y ,numbers,10)
print(result) # 输出 240 (10 * 1 * 2 * 3 * 4)


# zip:用于将多个可迭代对象中的元素按位置配对，生成由元组组成的迭代器
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result=zip(list1,list2) # 每个位置元素匹配之后生成一个元素
print(list(result)) #  [(1, 4), (2, 5), (3, 6)]

for a,b in zip(list1,list2):
    print(a,b)

list3=[7,8]
result=zip(list1,list3)
print(list(result)) # 输出 [(1, 7), (2, 8)]，超出的元素被忽略

# 结合使用
list1 = [1, 2, 3]
list2 = [4, 5, 6]
multiplied =map(operator.mul,list1,list2)
print(list(multiplied))

sum_op_products=reduce(operator.add,map(operator.mul,list1,list2))
print(sum_op_products)