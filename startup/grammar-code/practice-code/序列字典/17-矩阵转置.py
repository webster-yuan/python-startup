a,b=[int(x) for x in input().split()]
num=list()
x=y=0
for i in range(a):
    num.append(list(map(int,input().split())))
for i in range(b):
    for h in range(a):
        print(num[h][i],end=' ')
    print(' ')
