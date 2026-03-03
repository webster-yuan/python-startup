# 装饰器的返回值也是一个函数对象，本质上就是一个闭包函数
# 用于功能升级
# 在不改变原有代码的情况下，添加新的功能
# 不改变函数或者程序的调用方法

# 需要添加的函数
def register():
    print("注册")

def login():
    print("登录")

def root(fn):
    print("首页")
    fn()

root(login)
# 首页
# 登录
# 我想给root添加新的功能登录，原来的调用方式是root()，现在改变了调用方式，才实现了新增登录的功能

# 闭包的三个条件
# 1. 函数嵌套
# 2. 内函数使用了外函数的局部变量
# 3. 外函数的返回值是内函数的函数名

# 装饰器函数
def outer(fn):
    def inner():
        login() # 新加功能
        register()

        fn() # 原有功能，send，被装饰的函数

    return inner

# 被装饰的函数
def send():
    print("发送消息")

# 装饰器原理：就是将原有函数名重新定义为以原函数为参数的闭包

# 标准装饰操作，比较麻烦
ot = outer(send)
ot()

# 语法糖：
# @装饰器函数名称
# 被装饰的函数定义

@outer  # 没有()，是装饰器函数名，引用
def write():
    print("写")

write()
# 登录
# 注册
# 写

# 装饰器函数
def airpods(fn):
    def wrapper(message):
        print(f"用AirPods听:{message}")
        fn(message)
    
    return wrapper

# 被装饰的函数存在参数
@airpods # 语法糖形式
def listen(message):
    print(f"listen message is {message}")


listen("雨天")

# 用AirPods听:雨天
# listen message is 雨天

# 标准装饰格式
listen_by_airpods = airpods(listen)
listen_by_airpods("我怀念的")
# 用AirPods听:我怀念的
# 用AirPods听:我怀念的
# listen message is 我怀念的


def organized(fn):
    def wrapper(*args, **kwargs):
        print("做事情需要有组织的，调理清晰的")
        fn(*args, **kwargs)
    
    return wrapper

# 被装饰函数有可变参数，关键字函数
@organized
def work(*args, **kwargs):
    print(f"args:{args}, kwargs:{kwargs}")

work("webster", age=25, sex="male")

# 做事情需要有组织的，调理清晰的
# args:('webster',), kwargs:{'age': 25, 'sex': 'male'}

organized_work = organized(work)
organized_work("webster", age=25, sex="male")


# 多个装饰器
# 多个装饰器的装饰过程，离函数最近的装饰器先装饰，外面的装饰器再进行装饰

def deco1(fn):
    def wrapper():
        print("deco1 begin")
        res = fn()
        print("deco1 end")
        return res
    
    return wrapper

def deco2(fn):
    def wrapper():
        print("deco2 begin")
        res = fn()
        print("deco2 end")
        return res
    
    return wrapper
    

@deco1
@deco2
def custom_func() -> str:
    print("执行custom_func")
    return "custom_func"

custom_func()

# deco1 begin
# deco2 begin
# 执行custom_func
# deco2 end
# deco1 end

# deco1(deco2(custom_func))
# deco2中 保留返回值：装饰器的 wrapper 函数必须返回 fn() 的结果（result），否则原函数的返回值会丢失（变成 None）
# 再在deco1装饰的时候，就会变为None
# 装饰器的核心是 “增强原函数”，而非替代，要保证原函数的功能（比如返回值）不受影响。