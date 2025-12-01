# 当读取文件内容时,不建议直接读取到内存中,
# 如果文件内容很大，会导致内存占用激增
with open('test1.txt','r') as file:
    lines = file.readlines() # 返回一个list
    for line in lines:
        print(line.strip())
        
# 正确写法
with open('test.txt','r') as file:
    for line in file: # 直接遍历对象,无需读入整个文件
        print(line.strip())
        
# 判断元素是否存在
# in 是基于哈希表的,对于字典和集合,查找速度更快
my_dict={'a':1,'b':2}
if 'a' in my_dict:
    print("1")

my_list=[1,2,3,4,5]
if 3 in my_list:
    print("1")

# 删除列表元素时,应该使用返回list的方式
# 直接在迭代器上修改容器(列表)可能会引发RuntimeError
# 所以建议先将容器转换为列表的副本,在进行遍历和修改
# # 1. 错误
my_list=[1,2,32,4,5]
for item in my_list:
    if item%2==0:
        my_list.remove(item)

for item in my_list[:]: # 通过切片的方式生成副本
    if item%2==0:
        my_list.remove(item)
