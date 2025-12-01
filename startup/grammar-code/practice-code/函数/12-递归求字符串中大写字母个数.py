def countUppercase(list):
    num=0
    for i in list:
        if i.isupper():
            num+=1
    return num


list=input()
print(countUppercase(list))