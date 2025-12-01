n = int(input())


# 定义函数求阶乘
def jiecheng(n):
    num = 1
    for x in range(1, n + 1):
        num = x * num
    return num


sum_num = 0
for i in range(1, n + 1):
    sum_num += jiecheng(i)
print(sum_num)
