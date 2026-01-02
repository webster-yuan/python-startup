# 文件操作

# 写入文件
with open("example.txt","w") as file:
    file.write("hello world")

# 读取文件
with open("example.txt","r" )as file:
    content =file.read()
    print(content)

# 追加内容
with open("example.txt","a") as file:
    file.write("\nhello again")
