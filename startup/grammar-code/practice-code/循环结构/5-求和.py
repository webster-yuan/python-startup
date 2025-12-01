x=int(input())
b=0
for i in range(1,x+1) :
    if i%2==0 :
        c=1
    else :
        a=i*(i+1)
        b=b+a
print(b)
