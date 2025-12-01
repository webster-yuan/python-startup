str_num=str(input())

def inthis(str_num):
    if ord(str_num)>=48 and ord(str_num)<=57:
        return True
    elif ord(str_num)>=97 and ord(str_num)<=122:
        return True
    elif ord(str_num)>=65 and ord(str_num)<=90:
        return True
    elif ord(str_num)==45 or ord(str_num)==43:
        return True
    elif str_num=='*' or str_num=='#':
        return True
    else:
        return False

def zhuanhua(str_num):
    if (ord(str_num)>=97 and ord(str_num)<=122) or (ord(str_num)>=65 and ord(str_num)<=90):
        if (ord(str_num)>=97 and ord(str_num)<=99) or (ord(str_num)>=65 and ord(str_num)<=67):
            return '2'
        elif (ord(str_num)>=100 and ord(str_num)<=102) or (ord(str_num)>=68 and ord(str_num)<=70):
            return '3'
        elif (ord(str_num)>=103 and ord(str_num)<=105) or (ord(str_num)>=71 and ord(str_num)<=73):
            return '4'
        elif (ord(str_num)>=106 and ord(str_num)<=108) or (ord(str_num)>=74 and ord(str_num)<=76):
            return '5'
        elif (ord(str_num)>=109 and ord(str_num)<=111) or (ord(str_num)>=77 and ord(str_num)<=79):
            return '6'
        elif (ord(str_num)>=112 and ord(str_num)<=115) or (ord(str_num)>=80 and ord(str_num)<=83):
            return '7'
        elif (ord(str_num)>=116 and ord(str_num)<=118) or (ord(str_num)>=84 and ord(str_num)<=86):
            return '8'
        elif (ord(str_num)>=119 and ord(str_num)<=122) or (ord(str_num)>=87 and ord(str_num)<=90):
            return '9'
        elif ord(str_num)==ord('+'):
            return '0'
    else:
        return str_num
n=0
for x in range(0,len(str_num)):
    if inthis(str_num[x]):
        n+=1
if(n==len(str_num)):
    for x in range(0,len(str_num)):
        print(zhuanhua(str_num[x]),end='')
else:
    print(str_num,'invalid')
        
