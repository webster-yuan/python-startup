# 惰性加载数据（内存优化）

# 典型应用：处理大型文件、数据库分页查询、无限序列

def db_query(sql:str, page:int,size:int):
    return {}


def paginated_query(sql, page_size:int=100):
    page = 0
    while True:
        data = db_query(sql, page=page, size=page_size)
        if not data:
            break
        yield data
        page += 1

for batch in paginated_query("SELECT * FROM users"):
    print(batch)