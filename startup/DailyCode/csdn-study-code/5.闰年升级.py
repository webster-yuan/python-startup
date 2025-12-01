# 能被4整除 && 不能被100整除
# 能被400整除

year=int(input("请输入年份："))
month=int(input("请输入月份："))
day=int(input("请输入日期："))

date_list=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
count_day=day
if year %4==0 and year %100!=0 or year%400==0:
    print("%s年是闰年"%year)
    date_list[1]=29
else:
    print("%s年是平年"%year)
    date_list[1]=28
# 计算是当前的第几天
for i in range(month-1):
    count_day += date_list[i]

print("%s年:%s月:%s日是当年的第%s天" % (year,month,day,count_day))

