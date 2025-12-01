h,m=[int(x) for x in input().split()]
j1=h*30+(m/60)*30
j2=m*6
j=j2-j1
if j<0:
    j=-j
if j>180:
    j=360-j
print(format(j,'.1f'))