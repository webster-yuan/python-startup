str_1=str(input())
str_2=str(input())
n=0
for x in range(0,len(str_1)):
    if str_2==str_1[x]:
        n+=1
print(n)