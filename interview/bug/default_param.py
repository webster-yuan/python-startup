import datetime
import time

# 1. 例子一：
class Solution:
    def __init__(self, date=datetime.datetime.now()):
        """
        Python 为了性能优化，默认参数的求值结果会被缓存，而非每次实例化都重新执行一次求值表达式。
        这意味着在类定义时，date 参数的默认值会被计算一次，
        并且所有实例都会共享这个默认值。
        因此，S1 和 S2 实例的 date 属性都指向同一个 datetime 对象，
        这就是为什么它们的 date 属性相同的原因。
        """
        self.date = date


S1 = Solution()
print(S1.date)
time.sleep(1)
S2 = Solution()
print(S2.date)
# 2026-03-17 15:25:10.194564
# 2026-03-17 15:25:10.194564


# 2. 例子二：

def add_item(item, lst=[]):
    """
    默认参数 lst=[] 在函数定义时创建一个空列表，
    后续所有调用都复用同一个列表对象（列表是可变对象，append 会修改原对象）。
    """
    lst.append(item)
    return lst

# 多次调用，列表会持续累积值
print(add_item(1))  # [1]
print(add_item(2))  # [1, 2]（预期是 [2]）
print(add_item(3))  # [1, 2, 3]（预期是 [3]）


# 3. 例子三：

def create_functions():
    """
    正确写法：使用默认参数 j=i 来捕获当前循环变量的值，
    都会创建一个新的空间存储i的值，然后把引用返回给到j，func 内部访问的就是 j 的值，而不是 i 此时的值。
    所以每个 func 都会正确返回它被创建时 i 的值，而不是循环结束时 i 的值。
    所以是预期的 [0, 1, 2]。
    """
    funcs = []
    for i in range(3):
        # 默认参数 j=i 在循环时（函数定义时）求值，每次 i 不同
        def func(j=i):
            return j
        funcs.append(func)
    return funcs

# 预期 [0,1,2]，实际也能得到，但如果写错成 j=i（非默认参数）就会踩坑：
def create_functions_error():
    """
    错误写法：func 内部访问的 i 是一个闭包引用，循环结束后 i 的值是 2，
    所有 func 都引用 同一个外部变量 i，在结束时引用指向的地址的值是2，
    所以无论调用哪个 func，访问的都是 i 的值 2，而不是创建 func 时 i 的值。
    所以预期的 [0, 1, 2]，实际却是 [2, 2, 2]。
    """
    funcs = []
    for i in range(3):
        def func():
            return i  # 非默认参数，i 是闭包引用，循环结束后 i=2
        funcs.append(func)
    return funcs

funcs = create_functions_error()
# funcs = [func, func, func]，每个 func 内部访问的 i 都是同一个外部变量 i，循环结束时 i=2
print(funcs[0]())  # 2（预期 0）
print(funcs[1]())  # 2（预期 1）

funcs = create_functions()
# funcs = [func, func, func]，每个 func 内部访问的 i 都是同一个外部变量 i，循环结束时 i=2
print(funcs[0]())  # 0（预期 0）
print(funcs[1]())  # 1（预期 1）



# 4. 例子四：
def modify_list(lst):
    """
    lst.append(1) 修改了传入的列表对象（可变对象），所以 my_list 也被修改了。
    lst = [2,3] 重新赋值了 lst 变量，使其指
    向一个新的列表对象，但这不会影响 my_list，因为 my_list 仍然指向原来的列表对象。
    因此，最终输出的 my_list 是 [0, 1]，而不是 [0
    """
    lst.append(1)  # 修改原列表
    lst = [2,3]    # 重新赋值（仅改变局部变量指向）

my_list = [0]
modify_list(my_list)
print(my_list)  # [0,1]（预期 [0]，append改了原对象；重新赋值不影响）