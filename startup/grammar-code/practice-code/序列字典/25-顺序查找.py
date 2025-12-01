num=list(map(int,input().split()))
num_1=num[0:-1]
num_2=num[-1]
for i in range(len(num_1)):
    if num_2==num_1[i]:
        print(i)
        break
else:
    print(num_2,'no')