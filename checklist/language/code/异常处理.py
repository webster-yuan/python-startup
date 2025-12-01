
try:
    result=10/0
except ZeroDivisionError as e:
    print(f"捕获异常:{e}")
    raise #重新抛出异常,交给最高层逻辑处理

def read_file(file_path):
    try:
        with open(file_path,'r') as file:
            data=file.read()
        return data
    except FileNotFoundError:
        print("文件未找到,请检查路径")
    except PermissionError:
        print("没有权限访问该文件")

# 使用基于对象的异常,不只是字符串
class CustomError(Exception):
    pass

raise CustomError("自定义异常")

# raise "这是个错误的抛出异常"

class MyModuleError(Exception):
    """模块通用异常基类"""
    pass

try:
    raise ValueError("无效的值")
except ValueError:
    print("捕获到value error")
finally:
    print("执行清理操作")
    
# 捕获多个异常,使用括号
try:
    result=int(input("输入一个整数# "))
except (ValueError,TypeError) as e:
    print(f"捕获到异常:{e}")
    