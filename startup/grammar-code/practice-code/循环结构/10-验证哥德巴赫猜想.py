
from operator import truediv

#判断是否为素数
def prime_number(num):
    for x in range(2,num):
        if num%x==0:
            return False
    return True

num=int(input())
for x in range(3,(num//2)):
    if prime_number(x):
        y=num-x;
        if prime_number(y):
            print(x,y)
        
