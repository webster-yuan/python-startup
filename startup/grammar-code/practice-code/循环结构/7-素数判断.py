a=int(input())
flag=0
for i in range(2,a) :
    if a%i==0 :
        print(a,'No')
        flag=1
        break
if flag==0 :
    print(a,'Yes')
