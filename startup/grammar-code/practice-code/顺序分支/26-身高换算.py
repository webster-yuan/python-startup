x,y=[int(x) for x in input().split()]
h=x*0.3048+y*0.3048/12
if h<1.7:
    print(format(h,'.2f'),'you are short')
elif 1.7<=h<=2.25:
    print(format(h,'.2f'),'you are middle')
elif h>2.25:
    print(format(h,'.2f'),'you are tall')