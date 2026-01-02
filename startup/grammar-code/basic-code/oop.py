
class Person:
    def __init__(self,name,age): # __init__方法作用是初始化Person类的属性
        self.name=name
        self.age=age
    def greet(self): # greet方法作用是返回一个问候语
        return f"Hello, my name is {self.name} and I am {self.age} years old."
person1 = Person("yuanwei",22)
print(person1.greet())

