a=list(map(int,input().split()))
min=a[0]
max=a[0]
for i in a:
    if i<min:
        min=i
    if i>max:
        max=i
print(max,end=' ')
print(min)