# 列表
list_example = [1, 2, 3, 4]

# 元组
tuple_example = (1, 2, 3)

# 字典
dict_example = {"name": "yw", "age": 23}

# 集合
set_example = {1, 2, 3, 4}

x = 10
# if条件语句
if x > 0:
    print("x is positive")

for i in range(5):
    print(i)

count = 0
while count < 5:
    print(count)
    count += 1

def greet(name):
    return "Hello "+ name+"~"

print(greet("yw"))

import math
print(math.sqrt(16))

try:
    result = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero")

# 文件操作
with open("example/txt","w") as file:
    file.write("hello yw")
with open("example.txt","r") as file:
    content = file.read()
    print(content)