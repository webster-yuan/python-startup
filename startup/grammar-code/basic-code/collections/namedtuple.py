# 核心是创建具名元组—— 既保留了普通元组的不可变特性，又能通过「字段名」访问元素（而非仅靠索引）
# 对比普通元组：无需记忆元素索引（如用person.name代替person[0]），可读性大幅提升；
# 对比字典：不可变（避免意外修改数据）、占用内存更小、访问速度更快，且自带便捷的序列化方法；
# 对比自定义类（class）：无需编写__init__、__repr__等模板代码，代码更简洁轻便

from collections import namedtuple

# typename: 具名元组的类名（字符串类型）
# field_names: 指定具名元组的字段名
#   字符串列表 / 元组: ["name", "age", "gender"]
#   空格 / 逗号分隔的字符串: "name age gender"
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

Person = namedtuple('Person', "name age")
person = Person("John", "19")
print(person.name)  # John
print(person.age)  # 19
