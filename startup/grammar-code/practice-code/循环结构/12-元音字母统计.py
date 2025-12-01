a=input()
n=0
for i in range(0,len(a)):
    if ord(a[i])==97 or ord(a[i])==101 or ord(a[i])==105 or ord(a[i])==111 or ord(a[i])==117:
        n=n+1
print(n)
