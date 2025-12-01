
# Python 中，空容器（如 []、()、{}）、空字符串、None、0 等本身在布尔上下文中会被解释为 False。
# 明确写出 != [] 是多余的，增加了阅读成本。

users=[]
if not users:
    print("1")
    
# 不推荐
if users !=[] :
    print("2")
    
value=None
if value is None:
    print("value is None")

if value is not None:
    print("value is not None")


# 检查value=[]在后续是否被重新赋值
if value:
    print("3")
# 替代
if value is not None and value:
    print("4")
    

# 不将bool值使用==和False比较
flag = False
if not flag:
    print("11")

# 区分False 和 None时要明确逻辑
value=None
if not value and value is not None:
    print("value is False but not None")
    
# 序列的布尔求值
# 空序列的布尔值为 False，非空序列为 True，无需显式调用 len(seq)
users=[]
if not users:
    print("no users")
    
# 不推荐
if len(users)==0:
    print("no users")
    
# 整数布尔求值:None 和 0 都在布尔上下文中为 False，但它们是不同的语义
value =0
if value==0:
    print("value is zero")

# 不推荐:隐式判断会导致误判
value =None
if not value:
    print("Value is zero or None")
    
# 特殊值注意事项 "0"
# 字符串 "0" 是非空字符串，因此在布尔上下文中为 True。
value="0"
if value:
    print("String '0' is True in Boolean context")  # 输出此行
    
x=0
if x is 0:
   print("1") 
   
   
def multi(count):
    for i in range(count):
        yield lambda x, i=i: i * x  # Capture i by default argument

d = [v(k) for k, v in zip(range(4), multi(4))]
print(" ".join(map(str, d)))
