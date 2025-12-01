def reverseDisplay(s):
    i=len(s)-1
    return reverseDisplayHelper(s,i)
    
def reverseDisplayHelper(s,high):
    if high==-1:
        return
    else:
        print(s[high],end='')
        reverseDisplayHelper(s,high-1)


if __name__=="__main__":
    s=input()
    reverseDisplay(s)

