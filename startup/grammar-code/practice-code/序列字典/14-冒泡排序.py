lst=list(map(int,input().split()))

for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            lst[i],lst[j]=lst[j],lst[i]
for i in range(0,len(lst)):
    print(lst[i],end=' ')
