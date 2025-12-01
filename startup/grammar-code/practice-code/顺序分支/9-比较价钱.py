a1,a2=[float(x) for x in input().split()]
b1,b2=[float(x) for x in input().split()]
a=a2/a1
b=b2/b1
if a<b:
    print(format(a1,'.0f'),end=' ')
    print(format(a2,'.1f'))
else:
    print(format(b1,'.0f'),end=' ')
    print(format(b2,'.1f'))