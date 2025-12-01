a=int(input())
b=200
c=100
d=50
for i in range(1,a):
    c=c+b/2
    b=b/2
    d=d/2
print(format(c,'.2f'),end=' ')
print(format(d,'.2f'))