def panduan(num,width):
    if width<=len(str(num)):
        print(num)
    else:
        n=width-len(str(num))
        if num>0:
            for i in range(n):
                print('0',end='')
            print(num)
        else:
            print('-',end='')
            for  i in range(n):
                print('0',end='')
            print(-num)



num,width=[int(x) for x in input().split()]
panduan(num,width)