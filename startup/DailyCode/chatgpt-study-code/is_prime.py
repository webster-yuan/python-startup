# 判断是否是素数
def is_prime(n):
    if n<=1:
        return False;
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False;
    return True;
        
    
number =int(input("Please enter a number:"))
if is_prime(number):
    print(number,"The number is prime!")
else:
    print(number,"The number is not prime!")