def isin(x,y):
    if x*x+y*y>4:
        return 1
    elif x*x+y*y==4:
        return 0
    else :
        return -1

if __name__=="__main__":
    x,y=[float(x) for x in input().split()]
    if isin(x,y)==-1:
        print("{0:.2f} {1:.2f} in".format(x,y))
    elif isin(x,y)==0:
        print("{0:.2f} {1:.2f} on".format(x,y))
    elif isin(x,y)==1:
        print("{0:.2f} {1:.2f} out".format(x,y))
