def qiuhe(num,sum):
    sum=sum+num%10
    num=num//10
    if num>0:
        return qiuhe(num,sum)
    else:
        return sum



num=int(input())
if num<0:
    num=-num
print(qiuhe(num,0))