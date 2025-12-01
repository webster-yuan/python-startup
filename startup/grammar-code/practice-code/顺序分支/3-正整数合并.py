from ast import While


a,b=[int(x) for x in input().split()]
i=0
c=a%10*10+b%10
a=int(a/10)
b=int(b/10)
c=a*1000+b*100+c
print(c)
