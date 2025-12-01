

#求公约数给分子分母约分
def Approximately(num1,num2):
    temp=0
    while num2>0:
        temp=num1%num2
        num1=num2
        num2=temp
    return num1

str_1,str_2=[str(x) for x in input().split()]
for x in range(len(str_1)):
    if str_1[x]=='/':
        m=x
        break
for y in range(len(str_2)):
    if str_2[y]=='/':
        n=y
        break
num_11=int(str_1[0:m])
num_12=int(str_1[m+1:len(str_1)])
num_21=int(str_2[0:n])
num_22=int(str_2[n+1:len(str_2)])
num_1=num_11*num_22+num_21*num_12
num_2=num_12*num_22
num=Approximately(num_1,num_2)
print(int(num_1/num),end='')
print('/',end='')
print(int(num_2/num))
