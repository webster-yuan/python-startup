# 1
# st=[]
# st=input().split()
# n=len(st)
# book=[0]*20
# for i in range(0,n):
#     if int(st[i]) in range(10,20):
#         book[int(st[i])]=1
# # 判断10-20之间是否填满
# flag=True
# for i in range(10,20):
#     if book[i]!=1:
#         flag=False
#         break
# # 输出
# ret="("
# for i in range(0,n):
#     ret=ret+st[i]+","
# # 采用切片的方式，实现C++中str[9]="6"的修改字符串内容的操作
# # 因为python中str是不可变不可修改的，切片是将前多少个拿出来成为另一个字符串，覆盖ret实现上述功能
# ret=ret[:len(ret)-1]+")"
# if flag==True:
#     ret=ret+" cover all numbers"
# else:
#     ret=ret+" don't cover all numbers"
#
# print(ret)
# 2
# n=int(input())
# nameArr=[]
# adict={}
# for i in range(0,n):
#     name,height,weight=input().split()
#     nameArr.append(name)
#     #注意字典添加方式
#     adict[name]=adict.get(name,[height,weight])
# lowH,highH=map(int,input().split())
# lowW,highW=map(int,input().split())
# for name in nameArr:
#     h,w=adict.get(name)
#     height=int(h)
#     weight=int(w)
#     if height<lowH or height>highH:
#         h='*'+h
#     if weight<lowW or weight>highW:
#         w='*'+w
#     h=h+'cm'
#     w=w+'kg'
#     print(name+" "+h+" "+w)

#3
m, n = map(int, input().split())
s1 = set()
s2 = set()
all = []
for x in input().split():
    s1.add(x)
    all.append(x)
for x in input().split():
    s2.add(x)
    all.append(x)
print("所有跳高跳远运动员:", end = " ")
for x in sorted(all):
    print(x, end = " ")
print()
print("两项比赛都参加的有:", end = " ")
for x in sorted((s1 & s2)):
    print(x, end = " ")
print()
print("只参加跳高比赛的有:", end = " ")
for x in sorted((s1.difference(s2))):
    print(x, end = " ")
print()
print("只参加跳远比赛的有:", end = " ")
for x in sorted((s2.difference(s1))):
    print(x, end = " ")
print()
print("只参加一项比赛的有:", end = " ")
for x in sorted((s1.symmetric_difference(s2))):
    print(x, end = " ")
print()
