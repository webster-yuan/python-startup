x,y=[float(x) for x in input().split()]
if -5<=x<=5:
    if -3<=y<=3:
        print('Point (',end='')
        print(format(x,'.1f'),end=', ')
        print(format(y,'.1f'),end='')
        print(') is in the rectangle')
    else:
        print('Point (',end='')
        print(format(x,'.1f'),end=', ')
        print(format(y,'.1f'),end='')
        print(') is not in the rectangle')
else:
    print('Point (',end='')
    print(format(x,'.1f'),end=', ')
    print(format(y,'.1f'),end='')
    print(') is not in the rectangle')