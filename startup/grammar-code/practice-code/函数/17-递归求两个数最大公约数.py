def gongyue(num1,num2):
    if num1<num2:
        num1,num2=num2,num1
    num=num2
    num2=num1%num2
    num1=num
    if num2>0:
        return gongyue(num1,num2)
    else :
        return num1


if __name__=="__main__":
    num1,num2=[int(x) for x in input().split()]
    print(gongyue(num1,num2))
