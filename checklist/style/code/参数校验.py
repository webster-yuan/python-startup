
# 参数校验可以封装为函数,避免代码冗余
def validate_rectangle_params(length,width):
    """
    验证矩形参数

    Args:
        length (float): 矩形长度
        width (float):  矩形宽度
    Exceptions:
        TypeError: 当参数类型不正确时抛出。
        ValueError: 当参数值无效时抛出。
    """
    if not isinstance(length,(int,float)) or not isinstance(width,(int,float)):
        raise TypeError("长度宽度必须为数值类型")
    if length<=0 or width<=0:
        raise ValueError("长度宽度必须为正数")
    
def calculate_area(length,width):
    """
    计算矩形面积

    Args:
        length (float): 矩形长度
        width (float):  矩形宽度
    return:
    float:矩形面积
    """
    validate_rectangle_params(length,width)
    return length*width

