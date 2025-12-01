
# 嵌套类
class OuterClass:
    class InnerClass: # 嵌套类
        def __init__(self,value):
            self.value = value
        
    def create_inner(self,value):
            return self.InnerClass(value)

outer =OuterClass()    
inner = outer.create_inner(10)
print(inner.value)

# 改进
class InnerClass: # 嵌套类
    def __init__(self,value):
        self.value = value
    
class OuterClass:
    def create_inner(self,value):
            return self.InnerClass(value)

outer =OuterClass()    
inner = outer.create_inner(10)
print(inner.value)

# 局部类:定义在函数内部,用于函数的临时操作
def create_class_instance(value):
    class LocalClass: # 局部类
        def __init__(self,value):
             self.value = value
    
    return LocalClass(value)

instance = create_class_instance(10)
# 改进
class LocalClass: # 局部类
    def __init__(self,value):
            self.value = value

def create_class_instance(value):
    return LocalClass(value)

instance = create_class_instance(10)

# 内部函数:嵌套层次过深时会降低代码可读性
def process_data(data):
    def validate(data):
        if not isinstance(data,list):
            raise ValueError("data应为列表")
    validate(data)
    return [x*2 for x in data]
# 改进
def validate(data):
    if not isinstance(data,list):
        raise ValueError("data应为列表")

def process_data(data):
    validate(data)
    return [x*2 for x in data]

# 嵌套函数和类组合使用
def main_func():
    class HelperClass:
        def __init__(self,name):
             self.name=name

        def greet(self):
            return f"hello {self.name}"
    
    def helper_func(name):
        obj=HelperClass(name)
        return obj.greet()
    
    return helper_func("world")

print(main_func())
# 改进
class HelperClass:
    def __init__(self,name):
            self.name=name

    def greet(self):
        return f"hello {self.name}"

def helper_func(name):
    obj=HelperClass(name)
    return obj.greet()

def main_func():
    return helper_func("world")

print(main_func())