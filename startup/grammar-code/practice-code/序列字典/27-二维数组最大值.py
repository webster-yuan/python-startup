m,n=[int(x) for x in input().split()]
lis_num=[[0 for i in range(n)]for j in range(m)]
for i in range(m):
    lis_num[i]=list(map(int,input().split()))
a=b=max=0
for i in range(m):
    for j in range(n):
        if lis_num[i][j]>max:
            max=lis_num[i][j]
            a=i
            b=j
print(max,a,b)
