n=int(input())
a=int(n/100)
b=int(n/10%10)
c=n%10
if n==a*a*a+b*b*b+c*c*c:
    print(n,'yes')
else:
    print(n,'no')