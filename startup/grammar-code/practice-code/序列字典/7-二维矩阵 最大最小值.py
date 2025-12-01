a,b=[int(x) for x in input().split()]
num=list()
x=y=0
m=n=0
for i in range(a):
    num.append(list(map(int,input().split())))
max=num[0][0]
min=num[0][0]
for i in range(0,a):
    for h in range(0,b):
        if num[i][h]>max:
            max=num[i][h]
            x=i
            y=h
        if num[i][h]<min:
            min=num[i][h]
            m=i
            n=h
print("max[{0}][{1}]={2} min[{3}][{4}]={5}".format(x,y,max,m,n,min),end=' ')
