# 打印命令行参数
import sys

# 打印传递给脚本的命令行参数
print("Command line arguments:")
for arg in sys.argv:
    print(arg)
# python3 case1.py arg1 arg2 arg3
# Output:
# case1.py
# arg1
# arg2
# arg3