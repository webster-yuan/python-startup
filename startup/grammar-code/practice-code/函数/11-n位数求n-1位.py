def panduan(num,n):
    if len(str(num))==1 or num<0:
        print(num,'wrong')
    else:
        num=num-(num//(10**(n-1))*10**(n-1))
        print(num)




num=int(input())
n=len(str(num))
panduan(num,n)
