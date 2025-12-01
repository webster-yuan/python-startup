
str =input("请输入一串英文字母:")
dict={}
for i in str:
    dict[i]=dict.get(i,0)+1 # 统计出现次数,get()方法获取键对应的值，如果键不存在则返回默认值0,然后+1

for key ,value in dict.items():
    print('{0}:{1}'.format(key,value),end=' ') # 打印每个字母及其出现次数
print()