# 列表推导式练习

squares = [x**2 for x in range(10)]
print(squares)

# 输出：[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 练习1：将列表squares中的偶数平方，奇数不变
squares_even = [x**2 if x%2==0 else x for x in squares]
print(squares_even)

# 练习2: 将列表squares中的偶数平方，奇数加1
squares_even_plus1=[x**2 if x%2==0 else x+1 for x in squares]
print(squares_even_plus1)

# 练习3: 将列表squares中的偶数平方，奇数乘2
squares_even_times2=[x**2 if x%2==0 else x*2 for x in squares]
print(squares_even_times2)
