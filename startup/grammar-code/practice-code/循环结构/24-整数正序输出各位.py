m=int(input())
n=m
i=0
while m>0:
    m=m//10
    i+=1
t=0
i=i-1
while i>=0:
    t=n//(10**i)
    n=n-t*(10**i)
    i-=1
    print(t,end=' ')
