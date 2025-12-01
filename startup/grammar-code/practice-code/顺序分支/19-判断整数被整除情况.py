n=int(input())
if n%3==0 and n%5==0 and n%7==0:
    print('a',end=' ')
    print(n)
elif n%3!=0 and n%5!=0 and n%7!=0:
    print('c',end=' ')
    print(n)
else:
    print('b',end=' ')
    print(n)