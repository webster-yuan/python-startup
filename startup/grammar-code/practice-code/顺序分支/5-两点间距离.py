from cmath import sqrt


a,b,c,d=[float(x) for x in input().split()]
print(format(pow((c-a)*(c-a)+(d-b)*(d-b),0.5),'.2f'))