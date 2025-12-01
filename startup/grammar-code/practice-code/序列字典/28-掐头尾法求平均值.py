num=list(map(int,input().split()))
for i in range(len(num)-1):
    for j in range(i+1,len(num)):
        if num[i]>num[j]:
            num[i],num[j]=num[j],num[i]
new_num=num[2:-2]
sum=0
for i in new_num:
    sum+=i
print("{0:.2f}".format(sum/(len(new_num))))