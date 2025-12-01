def jishu(list,s):
    dic={}
    for i in list:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
        
    if s in dic:
        print(dic[s])
    else:
        print('0')



list,s=[str(x) for x in input().split()]
jishu(list,s)