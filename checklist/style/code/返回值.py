
# 不通过返回值判断函数运行正确性,而是使用抛异常的方式

def divide(a,b):
    """
    执行除法运算,若除数为0就抛异常

    Args:
        a (_type_): _description_
        b (_type_): _description_
    """
    if b==0:
        raise ValueError("除数不为0")
    return a/b

def func():
    try:
        result = divide(10,0)
    except ValueError as e:
        print(f"error:{e}")


# 错误方式如下
def diveide_wrong(a,b):
    if b==0:
        return None
    return a/b

def func_wrong():
    result=divide(10,0)
    if result is None:
        print("error,除数不为0")
        
# 返回值超过3个,使用dict,class
def get_user_info(user_id):
    """
    获取用户信息

    Args:
        user_id (_type_): _description_
    """
    return {
        "username":"a",
        "age":30,
        "email":"123@qq.com",
        "phone":"12345"
    }
def get_user_func():
    user_info = get_user_info(1)
    print(user_info["username"],user_info["email"])
    
    