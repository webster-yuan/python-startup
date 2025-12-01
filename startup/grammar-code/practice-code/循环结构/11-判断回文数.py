m=int(input())
n=m
i=0
while m>0:
    m=m//10
    i+=1
t=0
str1=str(n)
if i==1:
    print(str1,'yes')
else:
    for x in range(0,i):
        if str1[t]!=str1[i-1]:
            print(str1,'no')
            break
        else:
            t+=1
            i-=1
            if t==i or i-1==t:
                print(str1,'yes')
                break
