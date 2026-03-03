# 封装
# 隐藏属性,只允许在类的内部访问:在属性名或者属性方法前面加上两个下划线
# 隐藏属性实际上是修改为了: _类名__属性名 _Person__age
class Person:
    __name = "webster"
    __age = 25

    def get_name(self):
        """
        xxx方法/属性:类中定义,任何地方都可以调用
        """
        return Person.__name
    
    def get_age(self):
        return Person.__age
    
    def __watch(self):
        """
        双下划线开头,声明隐藏属性,类中定义,无法在外部访问,子类不会继承,
        访问只能通过间接的方式,在另外一个文件import时无法导入
        """
        print("隐藏方法:__watch")

    def _listen(self):
        """
        单下划线开头,私有属性/方法,类中定义,外部可以使用,子类会继承,
        在另外一个文件import时无法导入    
        """
        print("私有方法:_listen")

    def introduce(self):
        print("introduce")
        Person.__watch(self) # 在实例方法中调用隐藏方法


person = Person()
# person.__age
# person.__name
# AttributeError: 'Person' object has no attribute '__age'
print(person.get_name())

person.introduce()
# introduce
# 隐藏方法:__watch

person._listen()
# 私有方法:_listen

