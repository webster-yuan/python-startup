import itertools as it

print("无限偶数序列")

# 生成无限等差数列的迭代器函数，它会从指定的起始值开始，
# 按照固定的步长持续生成下一个数值，没有终止条件（除非手动停止迭代），
# 不会一次性生成所有值（惰性迭代），占用内存恒定
even = it.count(0, 2)

print(next(even))  # 0
print(next(even))  # 2
print(next(even))  # 4
print(next(even))  # 6

print(list(next(even) for _ in range(10)))
# [8, 10, 12, 14, 16, 18, 20, 22, 24, 26]

print("全排列")
for p in it.permutations('abc'):
    print(''.join(p), end=' ')

# 当手动指定r为小于元素总数n的正整数时，
# 生成的是从n个元素中取出r个元素的有序部分排列，
# 排列总数为A(n, r) = n×(n-1)×(n-2)×...×(n-r+1) 排列数公式

# r=2: ab ac ba bc ca cb
# r=None: abc acb bac bca cab cba
