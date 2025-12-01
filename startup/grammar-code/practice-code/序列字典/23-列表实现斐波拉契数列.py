n=int(input())
num_list=[0,1,1]
if n<=2:
    print(num_list[n])
else:
    for i in range(3,n+1):
        num_list.append(num_list[i-1]+num_list[i-2])
    print(num_list[i])

