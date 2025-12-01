a,b,c=[float(x) for x in input().split()]
if (a+b>c and b+c>a and a+c>b):
    s=(a+b+c)/2
    area=float(pow(s*(s-a)*(s-b)*(s-c),0.5))
    print(format(area,'.2f'))
else:
    print(format(a,'.2f'),end=' ')
    print(format(b,'.2f'),end=' ')
    print(format(c,'.2f'),end=' ')
    print('error')
