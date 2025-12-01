from posixpath import split


r,h=[float(x) for x in input().split()]
pi=3.14159
s=pi*r*r
v=s*h
print(format(v,'.2f'))
