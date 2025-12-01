

n =int(input("请输入你要打印的乘法表的阶数："))
for i in range(1,n+1): # [1,n] 其实就是[1,n+1)
    for j in range(1,i+1):
        print(f'{i}*{j}= {i*j}',end='\t')# 说明好每行结尾是\t，这样每行的输出格式更加美观
    print()
