def Fblq(num,fblq_list):
    
    fblq_list.append(fblq_list[-1]+fblq_list[-2])
    if len(fblq_list)>num:
        return print(fblq_list[num])
    else:
        return Fblq(num,fblq_list)



if __name__=='__main__':
    num=int(input())
    fblq_list=[0,1,1]
    Fblq(num,fblq_list)
