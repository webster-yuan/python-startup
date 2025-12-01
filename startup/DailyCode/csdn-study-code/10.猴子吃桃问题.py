# 猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个。
# 第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。
# 到第10天早上想再吃时，见只剩下一个桃子了。
# 求原来它一共摘了多少个桃子

# func函数返回第 n 天开始时的桃子数量
def func(n):
    if n==1:
        return 1
    return 2*(func(n-1)+1)

# func返回的是第n天的时候桃子的数量
def func2(n):
    if n==10:
        return 1
    return (func2(n+1) + 1 )*2

initial_count = func(10)
initial_count2 =func2(1)

print("初始摘了", initial_count, "个桃子")
print("初始摘了", initial_count2, "个桃子")