x=input().split()
max=x[0]
min=x[0]
z=0
i=0
h=0
for m in range(0,8):
    if x[m]>max:
        max=x[m]
        i=m
    elif x[m]<min:
        min=x[m]
        h=m
for m in range(0,8):
    if m!=i and m!=h:
        z=z+float(x[m])
z=float(z/6)
print(format(z,'.2f'))
