def qiuhe(n,k):
    sum=0
    for i in range(1,n+1):
        sum+=pow(i,k)
    return sum


if __name__=="__main__":
    n,k=[int(x) for x in input().split()]
    print(qiuhe(n,k))

