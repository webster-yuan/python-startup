s = input()
list_s = s.split()
list_num = [int(a) for a in list_s]
i=1
max=list_num[0]
num=1
while True:
    if list_num[i]==0:
        break
    if max<list_num[i]:
        max=list_num[i]
        num=1
    elif max==list_num[i]:
        num+=1
    i+=1
print(max,num)
