# 列出指定目录下的所有文件和目录

import os
# 获取当前工作目录
current_dir = os.getcwd()
print(f"当前工作目录:{current_dir}")
# 列出当前目录下所有的文件和目录
items =os.listdir(current_dir)
print(f"当前目录下的文件和目录:{items}")
for item in items:
    # 判断是否是文件
    if os.path.isfile(item):
        print(f"{item} 是文件")
    # 判断是否是目录
    elif os.path.isdir(item):
        print(f"{item} 是目录")
    else:
        print(f"{item} 不是文件也不是目录")