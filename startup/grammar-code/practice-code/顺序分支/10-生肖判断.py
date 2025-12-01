year=["dog","pig","rat","ox","tiger","rabbit","dragon","snake","horse","sheep","monkey","rooster"]
y=int(input())
n=y
y=y-2018
y=y%12
if y<0:
    y=-y
print(n,end=' ')
print(str(year[y]))
