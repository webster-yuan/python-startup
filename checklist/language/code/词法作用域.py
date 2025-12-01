
def outer():
    x=10
    
    def inner():
        print(f"x:{x}")
    
    inner()

outer()
# Outer variable x: 10


def outer():
    x=10
    
    def inner():
        print(f"x:{x}")
    
    inner()
    print(f"x:{x}")

outer()
# Inner x: 20
# Outer x: 10

# global声明全局变量
# 修改全局作用域中的变量
x=10
def modify_global():
    global x
    x=20
    
modify_global()
print(f"x:{x}")
# Global x: 20

# 使得嵌套函数能够修改外层函数的局部变量
def outer():
    x=10
    
    def inner():
        nonlocal x
        x=20
        print(f"inner x:{x}")
    
    inner()
    print(f"outer x:{x}")

outer()
# Inner x: 20
# Outer x: 20

def get_adder(summand1):
    """返回一个将数字加到指定值的函数"""
    def adder(summand2): # 通过 词法作用域 访问summand1
        return summand2+summand1
    
    return adder

add_five =get_adder(5)
print(add_five(10)) # 15

add_ten =get_adder(10)
print(add_ten(3))


