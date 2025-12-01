a=list(map(int,input().split()))
b=list(map(int,input().split()))
#print(" ".join(str(i) for i in a))
c=a
for i in b:
    if a.count(i)==0:
        c.append(i)
print(" ".join(str(i) for i in a))
# print(a)
# print(b)