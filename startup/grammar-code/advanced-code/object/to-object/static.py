# 静态方法
# 与类无关,可被转换为函数使用

class Person(object):
    @staticmethod
    def study(): # 无self cls等,减少内存占用和性能损耗
        print("study")

person = Person()
person.study()

Person.study()

# study
# study