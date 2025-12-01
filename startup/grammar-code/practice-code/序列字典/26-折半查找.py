num_list=list(map(int,input().split()))
num=num_list[-1]
num_list=num_list[:-1]
font=0
tail=len(num_list)
mid=tail//2
for i in range(tail):
    if num<num_list[mid]:
        tail=mid
    elif num>num_list[mid]:
        font=mid
    elif num==num_list[mid]:
        print(mid)
        n=1
        break
    mid=(font+tail)//2
    n=0
if n!=1:
    print(num,'no')
# 非递归

