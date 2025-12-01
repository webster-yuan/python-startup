num=int(input())
i=len(str(num))-1
new_num=0
while num>0:
    new_num+=num%10*10**i
    num=num//10
    i-=1
print(new_num)