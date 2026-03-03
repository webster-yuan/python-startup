# 类方法
# 使用装饰器@classmethod来标识类方法,第一个参数必须是cls

class Human:
    name = "webster"

    @classmethod
    def read(cls): # cls 代表类对象本身,可以访问类属性,类方法
        print(f"cls:{cls}")
        # cls:<class '__main__.Human'>
        print(cls.name)

human = Human()
human.read()
# 当方法中需要访问类对象,定义类方法,配合类属性使用