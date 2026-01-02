# 装饰器

def my_decorator(func):
    def wrapper(): # wrapper 作用: 包装函数, 增加功能
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper()

@my_decorator # 装饰器的使用
def say_hello():
    print("hello")

say_hello()