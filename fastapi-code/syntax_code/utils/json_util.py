import json


data = {
    "name": "张三",
    "age": 30,
    "is_student": False,
    "hobbies": ["阅读", "编程", "旅行"],
    "address": {
        "city": "北京",
        "postal_code": "100000"
    }
}

json_str = json.dumps(data)
print(json_str)

json_str2 = json.dumps(data, ensure_ascii=False) # 不转义非ASCII字符
print(json_str2)
json_str3 = json.dumps(data, indent=4, ensure_ascii=False) # 美化缩进4字符
print(json_str3)

json_obj = json.loads(json_str)
print(type(json_obj))
print(json_obj["name"])
print(json_obj["address"]["city"])


# 序列化自定义对象
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def custom_serializer(obj):
    if isinstance(obj, User):
        return {"name": obj.name, "age": obj.age}
    return TypeError(f"{type(obj)} not serializable")


def serializer():
    user = User("yuanwei", 23)
    print(json.dumps(user, default=custom_serializer))

def custom_deserializer_plus(dct):
    if isinstance(dct, dict):
        print(dct) # {'name': 'yuanwei', 'age': 23}
    if "name" in dct and "age" in dct:
        return User(dct["name"], dct["age"])
    return dct

def deserializer():
    json_data = '{"name": "yuanwei", "age": 23}'
    user = json.loads(json_data, object_hook=custom_deserializer_plus)
    print(type(user))
    print(user.name)


if __name__ == '__main__':
    deserializer()
