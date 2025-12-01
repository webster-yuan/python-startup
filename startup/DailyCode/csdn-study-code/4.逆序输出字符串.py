# 方式一：切片方式
# Python3 range() 返回的是一个可迭代对象（类型是对象），而不是列表类型
# range(start, stop[, step])
# 参数说明：
# start：计数从start 开始。默认是从0开始。例如range (5) 等价于range (0，5) ;
# stop：计数到stop结束，但不包括stop。 例如: range (0，5) 是 [0, 1, 2, 3, 4]没有5
# step：步长，默认为1。例如: range (0， 5) 等价于 range(0, 5, 1)
# range(5, 0, -1): [5, 4, 3, 2, 1]
# ->code:

# str_info =input('请输入字符串：')
# print ("逆序输出的结果是：",str_info[::-1])

# 方式二 循环转换
# 使用字符数组承接，然后进行拼接
str_info =input('请输入字符串：')
str_list=[]
for i in range(len(str_info)-1,-1,-1):
    str_list.append(str_info[i])
print("str_list: ",str_list)
print("逆序输出的结果是：",''.join(str_list))

