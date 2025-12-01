num=int(input())
num_lst=[1,2]
sum=0
for i in range(num):
    sum+=num_lst[i+1]/num_lst[i]
    num_lst.append(num_lst[i]+num_lst[i+1])
print("{0:.2f}".format(sum))