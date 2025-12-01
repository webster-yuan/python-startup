def fun(num1,num2):#求最大公约数
    t=0
    while num2>0:
        t=num1%num2
        num1=num2
        num2=t
    return num1
def lcm(x, y): #求最小公倍数
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm
a,b=[int(x) for x in input().split()]
print(fun(a,b),end=' ')
print(lcm(a,b))