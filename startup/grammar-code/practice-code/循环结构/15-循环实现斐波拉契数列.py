n=int(input())
a=b=1
if n==1 or n==2:
    print('1')
else:
    for i in range(2,n):
        m=a+b
        a=b
        b=m
if n!=1 and n!=2:
      print(m)
