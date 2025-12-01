import random


i=0
while i<3:
    print('请输入1~3分别代表剪刀、石头和布：', end='')
    x=random.randint(1,3)
    y=int(input())
    if x==1:
        print('计算机出剪刀，',end='')
        if y==2:
            print('您出石头，恭喜您赢了！')
            i+=1
        elif y==3:
            print('您出布，计算机赢。')
        else:
            print('您出剪刀，平局。')
    elif x==2:
        print('计算机出石头，', end='')
        if y == 2:
            print('您出石头，平局。')
        elif y == 3:
            print('您出布，恭喜您赢了！')
            i += 1
        else:
            print('您出剪刀，计算机赢。')
    else:
        print('计算机出布，', end='')
        if y==2:
            print('您出石头，计算机赢。')
        elif y==3:
            print('您出布，平局。')
        else:
            print('您出剪刀，恭喜您赢了！')
            i+=1