def jisuan(num):
    if num==0:
        print('1')
    elif num>=1:
        sum=1
        for i in range(num):
            sum+=3
        print(sum)

num=int(input())
jisuan(num)