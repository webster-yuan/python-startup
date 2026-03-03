# 继承: 子类继承父类的方法和属性
# class Child(Parent)

# 1. 单继承
class Person:
    def eat(self):
        print("eat")

    def sing(self):
        print("sing")

    def listen(self):
        print("listen")

class Girl(Person):
    pass

girl = Girl()
girl.sing()
# sing

# 2. 继承的传递(多重继承)
class Grandparnet:
    house = "house"

class Parent(Grandparnet):
    money = "money"

class Child(Parent):
    pass

child = Child()
print(f"money:{child.money}, house:{child.house}")
# money:money, house:house

# 3. 重写(覆盖):在子类中定义与父类相同的方法

class Human:
    def earn_money(self, n):
        print("赚钱")

class Male(Human):
    def earn_money(self):
        print("狠狠的赚钱")
    
male = Male()
male.earn_money()
# 狠狠的赚钱

# 4. 拓展: 继承父类的方法,子类自己拓展
class Animal:
    def eat(self):
        print("Animal eat")

    def __listen(self):
        print("Animal __listen")


class Dog(Animal):
    def eat(self):
        super().eat() # 使用super类创建的对象,可以访问父类的方法
        print("dog eat")


dog = Dog()
dog.eat()
# Animal eat
# dog eat

# 多继承
class Worker:
    def work(self):
        print("work")

    def money(self):
        print("Worker money")

class Son:
    def son(self):
        print("is a son")

    def money(self):
        print("Son money")

class Webster(Worker, Son):
    def learn(self):
        print("learn")

webster = Webster()
webster.learn()
webster.son()
webster.work()
# learn
# is a son
# work

webster.money()
# Worker money 所以多继承时,先看自己有没有,自己没有从左往右找继承的父类里面是不是有

# 多继承容易引发冲突，会导致代码设计的复杂度增加