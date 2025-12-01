num=list(map(int,input().split()))
if len(num)==1:
    print('list',num,'is already sorted')
else:
    for i in range(len(num)-1):
        if num[i]>num[i+1]:
            print('list',num,'is not sorted')
            break
        elif i==len(num)-2:
            print('list',num,'is already sorted')

