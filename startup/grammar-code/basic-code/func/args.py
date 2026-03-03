# 可变参数以元组的方式传递
def func1(*args):
    print(args)
    print(type(args))
    # ('aaa',)
    # <class 'tuple'>

func1("aaa")

# 关键字参数,以dict方式
def func2(**kwargs):
    print(kwargs)
    print(type(kwargs))
    # {'name': 'webster', 'age': 25}
    # <class 'dict'>

func2(name="webster",age=25)

# 全局变量作用域测试: 这样会报错
a =10

def test1():
    print(f"a:{a}")

def test2_v1():
    global a
    # 可以修改全局变量,也可以在局部作用域中声明个全局变量
    print(f"a:{a}")
    a = a + 20
    print(f"a:{a}")

def test2():
    a = a + 20 
    # error: 当 Python 解析test2()时，发现函数内有对a的赋值操作（a = ...），就会将a标记为该函数的局部变量，不再去全局作用域查找。
    # 但执行print(f"a:{a}")时，局部变量a还没被赋值（赋值操作在print之后），相当于 “引用了一个未定义的局部变量”，因此会抛出UnboundLocalError: local variable 'a' referenced before assignment（局部变量 a 在赋值前被引用）的错误。
    print(f"a:{a}")

test1()
test2_v1()
print(f"a:{a}") # 30