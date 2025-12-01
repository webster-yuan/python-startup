a,b,c=[int(x) for x in input().split()]
if (a+b>c and b+c>a and a+c>b):
    print(a,b,c,'yes')
else:
    print(a,b,c,'no')