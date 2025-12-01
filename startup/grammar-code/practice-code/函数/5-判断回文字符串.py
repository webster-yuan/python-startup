def huiwen(str):
    j=len(str)-1
    for i in range(len(str)//2):
        if str[i]!=str[j]:
            return False
        j-=1
    return True



if __name__=="__main__":
    str=input()
    if huiwen(str):
        print(str,'yes')
    else:
        print(str,'no')


