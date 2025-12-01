def Bbl(nextGuess,lastGuess,n):
    lastGuess=nextGuess
    nextGuess=(lastGuess+(n/lastGuess))/2
    if jueduizhi(nextGuess-lastGuess)<=0.00001:
        return print('{0:.5f}'.format(nextGuess))
    else:
        return Bbl(nextGuess,lastGuess,n)
# 绝对值
def jueduizhi(num):
    if num<0:return -num
    else:return num


if __name__=='__main__':
    n=float(input())
    lastGuess=1
    nextGuess=n
    Bbl(nextGuess,lastGuess,n)
