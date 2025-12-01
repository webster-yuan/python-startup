a,b,c=[float(x) for x in input().split()]
Delta=b*b-4*a*c
if Delta>0:
    print('x1=',end='')
    print(format((pow(Delta,0.5)-b)/(2*a),'.2f'),end=' ')
    print('x2=',end='')
    print(format(-(pow(Delta,0.5)+b)/(2*a),'.2f'),end=' ')
elif Delta==0:
    print('x1=',end='')
    print('x2=',end='')
    print(format(-b/(2*a),'.2f'))
else :
    print('x1=',end='')
    print(format((pow(Delta,0.5)-b)/(2*a),'.2f'),end=' ')
    print('x2=',end='')
    print(format(-(pow(Delta,0.5)+b)/(2*a),'.2f'),end=' ')
