import random
# 玩法一: 限制次数猜测
number = random.randint(0,100)
for i in range(10):
    choice = int(input("请输入你想猜测的数字："))
    if(choice > number):
        print("你猜大了")
    elif choice < number:
        print("你猜小了")
    else:
        print("你猜对了")
        print(f'你一共使用了{i}次机会')
        break
    print(f"还剩下{9-i}次机会")
else:
    print("游戏结束，你没猜中")
# 玩法二: 不限制次数猜测
number = random.randint(0,100)
count=0
while True:
    count += 1
    choice = int(input("请输入你想猜测的数字："))
    if(choice > number):
        print("你猜大了")
    elif choice < number:
        print("你猜小了")
    else:
        print("你猜对了")
        print(f'你一共使用了{i}次机会')
        break