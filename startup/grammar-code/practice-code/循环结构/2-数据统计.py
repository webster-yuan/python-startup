s = input()
list_s = s.split()
list_num = [int(a) for a in list_s]
x=y=0
i=0
num=0
while True:
    if list_num[i]==0:
        break
    elif list_num[i]>0:
        x+=1
    else:
        y+=1
    num=num+list_num[i]
    i+=1
print(x,y,num)