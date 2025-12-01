a,b=[int(x) for x in input().split()]
num=list()
x=y=0
for i in range(a):
    num.append(list(map(int,input().split())))
m=0
for i in range(0,b):
    for h in range(0,a):
       m=m+num[h][i]
    print(m,end=' ')
    m=0
