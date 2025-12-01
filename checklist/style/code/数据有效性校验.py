import os
# 文件数据检查
def read_and_validate_file(file_path):
    """读取文件并验证内容

    Args:
        file_path (_type_): 文件路径
    返回:
    list: 验证后的数据列表。
    异常:
    FileNotFoundError: 当文件不存在时抛出。
    ValueError: 当文件内容无效时抛出。
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件{file_path}不存在")
    
    with open(file_path,'r') as file:
        data=file.readlines()
    
    # 验证文件内容
    validated_data=[line.strip() for line in data if line.strip()]
    if not validated_data:
        raise ValueError("文件内容为空或者无效")
    
    return validated_data

# 数据库结果检查
def fetch_user_by_id(user_id,db_connection):
    """从数据库中获取用户信息并验证

    Args:
        user_id (int): 用户ID
        db_connection (object): 数据库连接对象
    返回:
    dict:用户信息
    异常:
    ValueError:当查询结果为空或者数据无效时抛出异常
    """
    cursor=db_connection.cursor()
    cursor.excute("sql")
    user = cursor.fetchone()
    
    if not user:
        raise ValueError(f"用户{user_id}不存在")
    
    return user
    
# 封装数据验证函数
def validate_user_data(data):
    """验证用户数据格式

    Args:
        data (_type_): _description_
    """
    required_keys=["id","name","email"]
    for key in required_keys:
        if key not in data:
            raise KeyError(f"缺少必要字段:{key}")
        
    if not isinstance(data["id"],int) or data["id"]<=0:
        raise ValueError("用户ID应为正整数")
    if '@' not in data['email']:
        raise ValueError("无效邮箱地址")
    
def process_user_data(raw_data):
    """处理用户数据,先进行验证

    Args:
        raw_data (_type_): _description_
    """
    validate_user_data(raw_data)
    return raw_data