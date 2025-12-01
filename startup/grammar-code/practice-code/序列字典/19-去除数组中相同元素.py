a=list(map(int,input().split()))
# for i in range(len(a)-1):
#     for j in range(len(a)-i-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
b=sorted(set(a),key=a.index)
print(" ".join(str(i) for i in b))