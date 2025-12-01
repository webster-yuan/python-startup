# 返回数组，数组中是前n个斐波那契数列的元素。
def fibonacci(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    fib_sequense=[0,1]
    for i in range(2,n):
        next_value=fib_sequense[i-1]+fib_sequense[i-2]
        fib_sequense.append(next_value)
    return fib_sequense

num_terms=int(input("Enter the count what you want to get in fibonacci series:"))
result=fibonacci(num_terms)
print(f"The first {num_terms} terms of fibonacci series are: {result}")