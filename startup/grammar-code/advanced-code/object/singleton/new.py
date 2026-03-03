# __new__是Object类内置的静态方法
# 1. 创建类并分配内存空间 2. 将引用返回给到__init__的cls中，让__init__进行初始化

class Human:
    def __init__(self):
        print("Human __init__")
    
    def __new__(cls, *args, **kwargs):
        print("__new__")
        # 继承父类的方法，并重写来验证new的执行顺序
        # 如果 __new__ 不返回当前类实例，则 __init__ 不会执行
        res = super().__new__(cls)
        return res

human = Human()
# __new__
# Human __init__