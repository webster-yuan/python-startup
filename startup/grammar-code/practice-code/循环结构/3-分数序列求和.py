n=int(input())
num=0.0
sum=0.0
for x in range(1,n+1):
    num=x+num
    sum = sum + (1 / num)
print(format(sum, '.2f'))
