def func1():
    raise Exception("exception")

func1()
print("can be made")
# Traceback (most recent call last):
#   File "E:\code\python-startup\startup\grammar-code\basic-code\exception\raise.py", line 4, in <module>
#     func1()
#   File "E:\code\python-startup\startup\grammar-code\basic-code\exception\raise.py", line 2, in func1
#     raise Exception("exception")
# Exception: exception