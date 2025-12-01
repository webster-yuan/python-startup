n=int(input())
if 0<n<1000:
    x=pow(n,0.5)
    if x%1!=0:
        y=10*x
        y=int(y%10)
        if y>=5:
            print(format(x,'.0f'))
        else:
            print(format(x,'.0f'))
    else:
        print(format(x,'.0f'))
else:
    print(n,'error')