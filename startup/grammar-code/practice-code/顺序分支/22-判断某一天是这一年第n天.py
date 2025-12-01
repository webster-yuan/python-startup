y,m,d=[int(x) for x in input().split()]
md1=[31,28,31,30,31,30,31,31,30,31,30,31]
md2=[31,29,31,30,31,30,31,31,30,31,30,31]
day=0
if (y%100!=0 and y%4==0) or y%400==0:
    for x in range(0,m-1):
        day=int(md2[x])+day
else:
    for x in range(0,m-1):
        day=int(md1[x])+day
day=day+d
print(day)
