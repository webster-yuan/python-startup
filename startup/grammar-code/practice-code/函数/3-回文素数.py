import math
# 素数判断
def prime_num(num):
    if num<2:
        return False
    for i in range(2,num//2):
        if num%i==0:
            return False
    return True

# 回文判断
def huiwen(num):
    num_str=str(num)
    j=len(num_str)-1
    for i in range(0,len(num_str)//2):
        if num_str[i]!=num_str[j]:
            return False
        j-=1
    return True

if __name__=='__main__':
    num=int(input())
    if prime_num(num) and huiwen(num):
        print(num,'yes')
    else:
        print(num,'no')
