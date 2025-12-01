#作业一
# import math
# a, b = input().split()
# a1,b1 =map(int,a.split('/'))
# a2,b2=map(int,b.split('/'))
# divisor=math.gcd(b1,b2)
# a1 *=b2//divisor
# a2 *=b1//divisor
# a1 +=a2
# b1 = b1*b2//divisor
# divisor = math.gcd(a1,b1)
# print("%d/%d" % (a1//divisor,b1//divisor))

#作业2
# str=int(input())
# temp=str
# pow=1#用于记录数字一共存在多少位
# while temp:
#     temp//=10
#     pow *=10
# pow//=10
#
# while pow:
#     num=str//pow
#     print(num,end=' ')
#     str-=num*pow
#     pow//=10

#作业三
# num=["me","mommy","daddy"]
# arr=[int(x) for x in input().split()]
# arr.sort()
# for i in range(3):
#     print(arr[i],num[i])

#作业四
# n = int(input())
# a = 0
# b = 1
# for i in range(n):#进来就是第一个
#     temp=b
#     b+=a
#     a=temp
# print(a)

#作业五
# n=input()
# begin=0
# end=len(n)-1
# while begin<end:
#     if(n[begin]!=n[end]):
#         break
#     else:
#         begin+=1
#         end-=1
# if(begin<end):
#     print("%d no"%int(n))
# else:
#     print("%d yes"%int(n))

#作业六
#哥德巴赫猜想
# import  math
# def IsPrime(n):
#     flag= True
#     for i in range(2,int(math.sqrt(n))+1):
#         if(n%i==0):
#             flag=False
#             break
#     return flag
#
# def Print(num):
#     n=len(num)
#     for i in range(n):
#         for j in range(2):
#             print(num[i][j],end=" ")
#         print("")#相当于换行
#
# def demo(n):
#     num=[]
#     if n>0 and n%2==0: #在偶数的前提下进行
#         for i in range(3,int(n/2)+1):
#             if(IsPrime(i) and IsPrime(n-i)):
#                 #以元组的方式进行存放
#                 # if (i,n-i) not in num:误将去重功能实现
#                 if i!=n-i:
#                     num.append((i,n-i))
#     Print(num)
#
# S=int(input())
# demo(S)

#作业7
# #a[-1]记录是F or C,采用的是逆序索引
# a=input()
# ch=a.split(a[-1])
# data=float(ch[0])
# if a[-1]=='F':
#     print("F=%.2lf" % (data*1.8+32))
# else:
#     print("C=%.2lf" % ((data-32)/1.8))
# #帮助理解95-97行
# # str=input().split('C')
# # 50C
# # >>> str
# # ['50', '']
# # >>> str[0]
# # '50'
# # >>>

#作业8
# #做法一：偷鸡
# a,b=input().split()
# print(a[0], end = '')
# print(b[0], end = '')
# print(a[1], end = '')
# print(b[1], end = '')
# #做法二：计算的话也没啥大用

#作业9
# arr= ["dog", "pig", "rat", "ox", "tiger", "rabbit", "dragon", "snake", "horse", "sheep", "monkey", "rooster"]
# n=int(input())
# print(n,arr[(n-2018)%12])

#作业10
wet1,val1=map(float,input().split())
wet2,val2=map(float,input().split())
if val1/wet1 < val2/wet2:
    print("%.0lf %.1lf" %(wet1,val1))
else:
    print("%.0lf %.1lf" %(wet2,val2))

