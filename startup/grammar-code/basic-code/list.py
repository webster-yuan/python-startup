# 列表的常用操作
fruits = ["apple","banana","cherry"]

print(fruits.index("banana")) # 找出指定元素的索引

fruits.append("date")
print(fruits)

fruits.insert(1,"grape") # 在指定位置插入元素
print(fruits)

fruits.remove("banana") # 删除指定元素,根据值删除
print(fruits)

fruits.pop(1) # 删除index的元素
print(fruits)

fruits.reverse() # 反转列表
print(fruits)

fruits.sort() # 排序列表,根据字母顺序
print(fruits)

fruits.sort(reverse=True) # 反向排序
print(fruits)

print(len(fruits)) # 列表长度

print(fruits[1]) # 访问指定位置的元素

print(fruits.count("apple")) # 统计指定元素出现的次数

fruits.clear() # 清空列表
print(fruits)
