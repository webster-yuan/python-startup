from datetime import datetime

def days_between_two_dates(date1, date2):
    d1=datetime.strptime(date1,"%Y-%m-%d")

    d2=datetime.strptime(date2,"%Y-%m-%d")
    delta=d2-d1
    return delta

date_str1=input("请输入第一个日期（格式：YYYY-MM-DD）：")
date_str2=input("请输入第二个日期（格式：YYYY-MM-DD）：")
days=days_between_two_dates(date_str1,date_str2)
print("两个日期间隔了{}天".format(days.days))