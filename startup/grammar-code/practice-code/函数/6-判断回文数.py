def huiwen(num):
    num_str=str(num)
    if num_str==num_str[::-1]:
        return True
    else:
        return False

if __name__=="__main__":
    num=int(input())
    if huiwen(num):
        print(num,'yes')
    else:
        print(num,'no')
