# 实例方法(Instance Method)是为了获取实例属性(self.attribute)
# 第一个参数必须是self,表示方法调用时自动传入的实例对象

class Person:
    def __init__(self,name): 
        self.name=name # 实例属性
        
    def greet(self):
        return f"hello {self.name}"
    
p =Person("Alice")
print(p.greet())

# 类方法 class method,使用装饰器@classmethod定义
# 第一个参数必须是cls,cls表示传入的是类本身
# 与类本身关联,用于操作类属性和类逻辑
class Student:
    species = "homo sapiens" # 类属性,所有实例共享
    
    @classmethod
    def get_species(cls): # 类方法直接操作类属性,与实例无关
        return f"Species :{cls.species}"

print(Student.get_species())
p=Student()
print(p.get_species())

# 静态方法: 适合是吸纳一些工具函数或者逻辑处理,与类有关但是不需要访问类本身的内容
class MathUtils:
    @staticmethod
    def add(a,b):
        return a+b
    
print(MathUtils.add(3,5))
m=MathUtils()
print(m.add(10,20))

# 构造方法:初始化类实例时调用,用于设置初始属性
class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
# 属性方法:@property
# 将实例方法伪装成属性,支持只读或只写
class Circle:
    def __init__(self,radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self,value):
        if value<0:
            raise ValueError("Radius must be none-negative")
        self.radius=value

# 运算符重载 * + - /
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    # 重载加法运算符
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)

# 字符串表示
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __str__(self):
        return f"Point({self.x},{self.y})"
    
    def __repr__(self):
        return f"Point({self.x},{self.y})"
    
# 迭代器协议
class Counter:
    def __init__(self,max_val):
        self.max_val=max_val
        self.current = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current>=self.max_val:
            raise StopIteration
        self.current+=1
        return self.current
    
# 上下文管理(__enter__,__exit__)
# 支持with语句,用于资源管理
class FileManager:
    def __init__(self,filename,mode):
        self.file=open(filename,mode)
        
    def __enter__(self):
        return self.file
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.file.close()
    
with FileManager("test.txt","w") as f:
    f.write("Hello World")
    