
my_str = 'I am$ N$iuniu$, an$d I $am stu$dying in $Now$coder!'
clean_str =my_str.replace('$',"")
print(clean_str)
# 将空格和$作为分隔符,将分割之后的结果放到list中,然后再将list中的元素连接成字符串

import re

# 定义字符串
my_str = 'I am$ N$iuniu$, an$d I $am stu$dying in $Now$coder!'

# 使用正则表达式分割字符串，匹配空格和$
split_list = re.split(r'[ \s$]+', my_str)

# 将列表中的元素连接成字符串，使用空格作为连接符
result_str = ' '.join(split_list)

# 打印结果
print(result_str)
