# 多态： 同一个行为，不同的状态
# 不同子类对象调用统一父类方法,产生不同的结果
# 发生在继承行为基础之上 + 重写

print(10+10)
print("10"+"10")
# 20
# 1010


class Animal:
    def shout(self):
        print("Animal is shouting")

class Dog(Animal):
    def shout(self):
        print("dog wang")

class Cat(Animal):
    def shout(self):
        print("cat wang")

cat = Cat()
cat.shout()
dog = Dog()
dog.shout()
# cat wang
# dog wang

def func1(animal:Animal):
    animal.shout()

func1(cat)
func1(dog)
# cat wang
# dog wang