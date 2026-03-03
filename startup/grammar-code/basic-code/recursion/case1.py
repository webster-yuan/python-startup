def add(n):
    s = 0

    for i in range(n+1):
        s+=i

    return s

print(add(10))

def recursion_add(n):
    if n ==1:
        return 1
    
    return n + recursion_add(n-1)

print(recursion_add(10))


# 1. Fib : 从第三项开始，每一项都等于前两项之和，前两项都是1
# 1 , 1, 2, 3, 5, 8 ...
def recursion_fib(n):
    """获取第N项Fib的值"""
    if n <=2:
        return 1
    
    return recursion_fib(n-2)+recursion_fib(n-1)

print(recursion_fib(4))

