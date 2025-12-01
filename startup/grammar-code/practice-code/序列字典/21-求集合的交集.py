a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in b:
    if a.count(i)==1:
        c.append(i)
#print(" ".join(str(i) for i in a))
print(" ".join(str(i) for i in c))
# print(a)
# print(b)