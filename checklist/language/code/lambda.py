# 匿名函数
square = lambda x:x**2

stus=[("alice",90),("bob",85),("cha",95)]
sorted_stus = sorted(stus,key=lambda x:x[1])
print(sorted_stus)

# 代替以下写法
sorted_students = sorted(stus, key=lambda x: x[1] if x[1] > 80 else 0)

# 推荐
def sorting_key(stus):
    return stus[1] if stus[1]>80 else 0

sorted_students=sorted(stus,key=sorting_key)
print(sorted_students)

# 建议:如果lambda表达式过长,使用普通函数替代

result = list(filter(lambda x:x%2 ==0 and x>10,range(100)))
print(result)

def is_valid(x):
    return x%2==0 and x>10

result=list(filter(is_valid,range(100)))
print(result)

# 建议使用operator模块中的函数,替代lambda
mul_result=list(map(lambda x:x*2,range(5)))
print(mul_result)

import operator
multi_result_=list(map(operator.mul,range(5),[2]*5))
print(multi_result_)


# operator.mul
list1 = [1,3,2]
list2 = [4,5,6]
result = list(map(operator.mul,list1,list2))
# 不推荐
result=list(map(lambda x,y: x*y,list1,list2))