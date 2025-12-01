a=int(input())
s=input().split()
k=int(input())
m=0
for i in range(0,len(s)):
    if k<int(s[i]) and m==0:
        print(k,s[i],end=' ')
        m=1
    else:
        print(s[i],end=' ')
if m==0:
    print(k)
