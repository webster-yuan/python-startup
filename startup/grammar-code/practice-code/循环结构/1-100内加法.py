import random

print('请输入练习题的数量：',end='')
n=int(input())
i=1
a = random.randint(0, 100)
b = random.randint(0, 100)
print(a, " + ", b, "= ?",end='')
x = int(input())
while i<n:
    if(a+b==x):
        i+=1
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        print(a, " + ", b, "= ?", end='')
        x = int(input())
    else:
        print('不对，请重新计算')
        print(a, " + ", b, "= ?",end='')
        x = int(input())

print('恭喜你完成此次加法练习')

