from cmath import sqrt


r,x,y=[float(x) for x in input().split()]
l=float(pow(x*x+y*y,0.5))
if l<=r:
    print('Point (',end='')
    print(format(x,'.1f'),end=', ')
    print(format(y,'.1f'),end='')
    print(') is in the circle')
else:
    print('Point (',end='')
    print(format(x,'.1f'),end=', ')
    print(format(y,'.1f'),end='')
    print(') is not in the circle')