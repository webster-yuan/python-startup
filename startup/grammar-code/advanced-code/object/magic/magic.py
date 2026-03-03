class Person:
    """类的描述信息"""
    pass

print(Person.__doc__) # 类的魔法属性，描述信息
# 类的描述信息

def sing():
    """唱歌"""
    pass

print(sing.__doc__) # 方法的描述信息
# 唱歌


# __module__ :返回对象的所属模块
# __class__ :返回对象的所属类

# __str__(): 返回对象的描述信息，必须返回一个字符串
class Human:
    def __str__(self):
        return "描述信息"

human = Human()
print(human)
# 描述信息

# __del__(): 析构函数调用，del删除对象的时候调用
# __call__(): 使得一个实例对象，成为一个可调用对象，类似于函数，类，凡是可以把一个()应用到某一个对象上，都可以成为可调用对象
def func1():
    print("1")

func1()
print(callable(func1))
# 1
# True 可调用对象

name = "abc"
print(callable(name))
# False 字符串不是可调用对象

class Animal:
    pass

animal = Animal()
print(callable(animal))
# False

class Dog:
    def __call__(self, *args, **kwds):
        print("call")

dog= Dog()
print(callable(dog))
# True
dog() # 就是在调用他的call方法
# call
# 用途：替代闭包
# 让对象具备函数调用方法的同时，保留内部状态
def make_counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count

# 装饰器类
class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("调用开始")
        result = self.func(*args, **kwargs)
        print("调用结束")
        return result

@Logger
def add(a, b):
    return a + b

print(add(1, 2))