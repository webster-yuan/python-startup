# 列出公因数
def gynum(num):
    num_lst=[]
    for i in range(1,num):
        if num%i==0:
            num_lst.append(i)
    return num_lst
# 判断完数
def wanshu(num,num_lst):
    sum=0
    for i in num_lst:
        sum+=i
    if sum==num:
        print("{0}=".format(num),end='')
        i=0
        while True:
            print(num_lst[i],end='')
            if i==len(num_lst)-1:
                break
            print('+',end='')
            i+=1
    elif sum>num:
        print("{0}<".format(num), end='')
        i = 0
        while True:
            print(num_lst[i], end='')
            if i == len(num_lst) - 1:
                break
            print('+', end='')
            i += 1
    elif sum<num:
        print("{0}>".format(num), end='')
        i = 0
        while True:
            print(num_lst[i], end='')
            if i == len(num_lst) - 1:
                break
            print('+', end='')
            i += 1

num=int(input())
num_lst=gynum(num)
wanshu(num,num_lst)
