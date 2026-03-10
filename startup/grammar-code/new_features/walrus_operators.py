# Python 3.8 引入了海象运算符（walrus operator），
# 用来在表达式内进行赋值。
# := 海象运算符，因为长得像海象的牙齿，所以得名
# 语法功能：在表达式内进行赋值
# 加()，是为了明确运算符优先级，避免歧义
# 优势：减少代码行数，避免重复调用函数，提高代码可读性


if (n:= len([1,2,3,4])) > 3:
    print(f"长度是 {n}，大于 3")

# 还可以在 while 循环中使用，避免重复调用函数
def get_next_item():
    # 模拟获取下一个项目的函数
    return input("请输入一个项目（输入 'exit' 退出）：")

while (item := get_next_item()) != 'exit':
    print(f"你输入了: {item}")