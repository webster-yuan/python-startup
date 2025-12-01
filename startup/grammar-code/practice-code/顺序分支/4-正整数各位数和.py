a=int(input())
c=a%10
a=int(a/10)
c=c+a%10
a=int(a/10)
c=c+a
print(c)