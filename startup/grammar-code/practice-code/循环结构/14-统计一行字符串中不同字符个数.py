n=input()
a=b=c=d=0
for i in n:
    if ord('a')<=ord(i)<=ord('z') or ord('A')<=ord(i)<=ord('Z'):
        a=a+1
    elif ord('0')<=ord(i)<=ord('9'):
        b=b+1
    elif ord(i)==ord(' '):
        c=c+1
    else:
        d=d+1
print(a,c,b,d)
