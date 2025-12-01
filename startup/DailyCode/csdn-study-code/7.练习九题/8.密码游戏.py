list =[]
num = input("请输入一个四位数:")
for i in num:
    number = (int(i)+3)%9
    list.append(number)

list[0],list[1],list[2],list[3] = list[2],list[3],list[0],list[1]
s ="".join(map(str,list)) # map作用是将list中的元素转化为字符串,再用join方法将字符串连接起来
print(s)