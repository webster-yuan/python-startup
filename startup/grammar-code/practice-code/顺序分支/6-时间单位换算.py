from re import A


t=int(input())
if t>=3600:
    h=int(t/3600)
    t=t%3600
else:
    h=0
    t=t%3600
if t>=60:
    m=int(t/60)
    s=t%60
else:
    m=0
    s=t%60
print(h,end='')
print(":",end='')
print(m,end='')
print(":",end='')
print(s)

