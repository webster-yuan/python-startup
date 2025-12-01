import math


def area(num,long):
    pi=3.1415926
    return (num*long*long)/(4*math.tan(pi/num))

num,long=[int(x) for x in input().split()]
print('{0:.2f}'.format(area(num,long)))