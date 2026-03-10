# 3.10 之后引入了 match-case 语句，类似于其他语言中的 switch-case，
# 但更强大，支持模式匹配，可以根据数据结构的形状进行匹配。
# int(x) 就是类型模式匹配，相当于 
# isinstance(data, int) 并且把 data 赋值给 x
# case type(x) 里的x是新绑定的局部变量，不会改变原始数据

def check_type(data):
    match data:
        case int(x) if x > 0:
            print(f"{x} is a positive integer")
        case str(s) if s:
            print(f"'{s}' is a non-empty string")
        case list(l) if l:
            print(f"{l} is a non-empty list")
        case _:
            print("Unknown type or empty value")

check_type(10)
check_type("hello")
# 10 is a positive integer
# 'hello' is a non-empty string