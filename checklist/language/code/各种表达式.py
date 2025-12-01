
# 列表推导式:返回的是一个列表
squares = [x*x for x in range(10)]
# 单层过滤
even_number=[x for x in range(10) if x%2==0]

# 使用生成器表达式
# 和列表推到式只有()的区别,返回的是生成器对象
# 惰性计算,只有用到时才会生成值
# 适合处理数据量较大的场景
processed=(x*x for x in range(1000) if x%2==0)

# 字典推导式
# 用于生成字典
squares={x:x*x for x in range(10)}
print(squares)

even_squares={x:x*x for x in range(10) if x%2==0}
print(even_squares)

# 集合推导式
sq1 = {x*x for x in range(10)}
unique_chars={char.lower() for char in "helloworld" if char.isalpha()}

# 条件表达式
x,y=10,20
max_value=x if x >y else y

# lambda表达式
square_ =lambda x:x*x
pairs =[(1,3),(2,2),(3,1)]
pairs.sort(key=lambda pair:pair[1])
print(pairs)