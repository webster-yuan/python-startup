def riqi():
    year,month,day=[int(x) for x in input().split()]
    month_list1=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    month_list2=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    sum_day=0
    if runnian(year):
        for i in range(month):
            sum_day+=month_list2[i]
    else:
        for i in range(month):
            sum_day+=month_list1[i]
    sum_day+=day
    print(sum_day)


def runnian(year):
    if year%400==0 or (year%100!=0 and year%4==0):
        return True
    else: return False

if __name__=="__main__":
    riqi()
