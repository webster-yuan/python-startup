m,n=map(int,input().split())
r=0
a=m
b=m*n
if m<n:
    m=n
    n=a
while 1:
    if m%n==0:
        break
    else:
        a=n
        n=m%n
        m=a
c=int(b/n)
print(n,c)
