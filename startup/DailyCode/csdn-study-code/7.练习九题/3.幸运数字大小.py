
a,b,c=map(int,input().split(',')) #map函数将输入的字符串转换为int类型
list1 =[a,b,c]
list2 =sorted(list1)
print("最小的数字为:",list2[0])
print("排序后的列表为:",list2)

