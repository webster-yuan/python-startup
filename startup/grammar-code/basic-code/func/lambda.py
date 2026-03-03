# 匿名函数
# 函数名=lambda 形参: 返回值（表达式）
# 调用：结果=函数名（实参）
# 本身就有返回，不需要return

add = lambda x,y:x+y

c = add(5,6)
print(c)

# 默认参数
func1 = lambda name, age=9:(name, age)
print(func1("webster"))
# ('webster', 9)

# 关键字参数
func2 = lambda **kwargs:kwargs
print(func2(name="webster",age=25)) 
# {'name': 'webster', 'age': 25}

# 结合if判断 lambda只适合简单的逻辑
cmp = lambda x,y : "x<y" if x<y else "x>=y"
print(cmp(5,6))
# x<y