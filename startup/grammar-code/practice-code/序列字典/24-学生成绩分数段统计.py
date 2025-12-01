a=list(map(int,input().split()))
b=c=d=e=f=0
for i in a:
    if i<=100 and i>=90:
        b=b+1
    if i<90 and i>=80:
        c=c+1
    if i<80 and i>=70:
        d=d+1
    if i<70 and i>=60:
        e=e+1
    if i<60 and i>=0:
        f=f+1
print(b,c,d,e,f,end=' ')