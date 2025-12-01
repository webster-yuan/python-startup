# 字典练习代码
person ={
    "name":"yuanwei",
    "age":22,
    "gender":"female"
}
print(person["name"])

person["age"]=31 # 根据字典key更新value
print(person)

# 字典的遍历
for key in person:
    print(key,person[key]) # 输出一个字典的所有key和value

# 字典的合并
person2 = {"name":"zhangsan","age":23}
person.update(person2)
print(person)

# 字典的添加
person["city"]="beijing"

# 字典的判断
if "name" in person:
    print("name is the elem of person class")

# 字典的删除
del person["age"]
print(person)
