
def is_prime1(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

# 优化版本
def is_prime2(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5+1)): # 优化，只需要检查到sqrt(n)即可
        if n%i == 0:
            return False
    return True

n = int(input("请输入一个正整数："))
flag = is_prime2(n)
if flag:
    print(n,"是素数")
else:
    print(n,"不是素数")

