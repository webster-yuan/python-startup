# 1. 定义一个类属性，存储单例对象的引用，保证内存地址不会发生改变来保证唯一性
# 2. 重写__new__()方法
# 3. 判断，如果类属性是None，把__new__()返回的对象引用保存
# 4. 返回类属性中记录的引用返回

class Singleton(object):
    instance = None
    def __new__(cls):
        if cls.instance is None:
            res = super().__new__(cls)
            cls.instance = res

        return cls.instance
    
    
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 == singleton2)
# True
