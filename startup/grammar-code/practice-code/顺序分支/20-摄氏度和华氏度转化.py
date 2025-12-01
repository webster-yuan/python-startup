a = input()
if a[-1] in ['F','f']:
    F = 1.8*eval(a[0:-1]) + 32
    print("F={:.2f}".format(F))
elif a[-1] in ['C','c']:
    C = (eval(a[0:-1]) - 32)/1.8
    print("C={:.2f}".format(C))
