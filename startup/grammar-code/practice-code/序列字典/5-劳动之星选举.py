n = int(input())
a = []
for i in range(0,n):
    b = list(input().split())
    a.append(b)
c = list(input().split())
kk = 0
for u in c:
    if c.count(u)>kk:
        kk = c.count(u)
        jj = int(u)
for hh in a:
    if kk ==c.count(hh[0]):
        print(hh[0],hh[1],hh[2])
