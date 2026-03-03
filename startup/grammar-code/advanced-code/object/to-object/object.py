class Washer:
    height = 800 # 类属性：类所拥有的属性


# 查看类属性:类名.属性名
print(Washer.height)
# 新增类属性:类名.属性名
Washer.width =450
print(Washer.width)

# 根据定义的类，创建对象也叫实例化对象
washer = Washer()
washer.height = 1000
print(f"Washer.height:{Washer.height}, washer.height:{washer.height}")
# Washer.height:800, washer.height:1000
print(f"id Washer.height:{id(Washer.height)}, washer.height:{id(washer.height)}")
# id Washer.height:2120221932720, washer.height:2120222956624
# 说明，类属性和对象访问的类属性，不是一个空间，说明每实例化一个对象，每个对象都会有自己的一份类属性拷贝


# 实例方法，实例属性:需要带上 self，代表对象（实例）本身，类中的实例方法必须具备self，才属于对象，实例化的对象才能调用
class Human:
    heigth = 1000
    def listen(self):
        print("listen...")
        print(self)
        # <__main__.Human object at 0x000002625B033EE0>

human = Human()
human.listen()
print(human)
# <__main__.Human object at 0x000002625B033EE0>
# 和 self 地址相同，所以self表示的就是当前实例化的对象本身，
# 当对象调用实例方法时，Python会自动将对象本身的引用，作为参数，传递到实例方法的第一个参数self上

# 实例属性： self.属性名 属于对象，只能由对象名访问，不能类名访问
# 类属性属于类，属于所有实例化的实例


# 构造函数:用于实例属性初始化/赋值操作，在类被实例化的时候自动调用
class Person:
    def __init__(self, name="webster", age=25, sex="male"): # self,实例方法
        print("这是__init__")
        self.name = name # 实例属性
        self.age = age
        self.sex = sex

person = Person()
# 这是__init__
print(f"person.name:{person.name}, person.age:{person.age}, person.sex:{person.sex}")
# person.name:webster, person.age:25, person.sex:male
person.name = "yuanwei"
print(f"person.name:{person.name}, person.age:{person.age}, person.sex:{person.sex}")
# person.name:yuanwei, person.age:25, person.sex:male

# 析构函数：对象在被回收的时候自动调用 __del__
class Cat:
    def __init__(self):
        print(f"我是__init__方法")
    
    def __del__(self):
        print(f"我是__delete__方法")
    
cat = Cat()
print("我是最后一行")
# 我是__init__方法
# 我是最后一行
# 我是__delete__方法
# del cat # 会立即调用cat本身的__del__方法