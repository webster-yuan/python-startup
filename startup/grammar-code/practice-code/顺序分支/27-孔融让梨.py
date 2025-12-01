a,b,c=[int(x) for x in input().split()]
list = [a,b,c]
for m in range(2):
    for n in range(m+1,3):
        if list[m]>list[n]:
            temp=list[n]
            list[n]=list[m]
            list[m]=temp
print(list[0],'me')
print(list[1],'mommy')
print(list[2],'daddy')
        