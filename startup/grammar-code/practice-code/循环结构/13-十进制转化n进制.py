def f(n,x):
    a=[0,1,2,3,4,5,6,7,8,9,'A','b','C','D','E','F']
    b=[]
    while True:
        s=n//x  # 商
        y=n%x  # 余数
        b=b+[y]
        if s==0:
            break
        n=s
    b.reverse()
    for i in b:
        print(a[i],end='')
a,b=map(int,input().split())
f(a,b)
