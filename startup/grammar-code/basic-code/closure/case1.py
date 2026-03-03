def outer():
    a = 10
    def inner():
        return a +10
    
    return inner

print(outer()) # 返回的是内部函数的地址
# <function outer.<locals>.inner at 0x0000028CDECEFAC0>
print(outer()()) # 使用()调用一下
# 20

def outer_with_args(n):
    m=10
    def inner_with_args(g):
        return n+m+g
    
    return inner_with_args # 返回函数名，不带()，也不要传参，如果inner参数比较多，写法不规范，所以在外层调用的时候传递

print(outer_with_args(n=20)(g=50))
# 80
# 函数名存放的是函数所在位置的引用
# id() 用来判断两个变量是否是同一个值的引用
a= 1 # a里面存放的就是存放1那个位置的地址，就是a存放了1的引用
print(id(a))
# 3168595542256
a=2 #
print(id(a))
# 3168595542288
print(id(2))
# 2315330257168


# 闭包：每次开启内函数，都在使用同一份闭包变量
