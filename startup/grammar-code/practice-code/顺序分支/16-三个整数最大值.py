a,b,c=[int(x) for x in input().split()]
if a>b:
    if a>c:
        print(a)
    else:
        if c>b:
            print(c)
        else:
            print(b)
else:
    if b>c:
        print(b)
    else:
        print(c)