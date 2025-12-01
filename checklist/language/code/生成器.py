# generator

# 使用yield在函数中逐步产生值,而不是一次将所有值返回
# 当返回较长列表需要大量计算时,优先使用生成器函数和yield而非返回整个列表
# 避免占用过多内存,提高性能(大数据流式计算)

def generator_func():
    for i in range(10):
        yield i # 每次调用时生成一个值
        
def infinite_sequence():
    i=0
    while True:
        yield i
        i+=1

gen = infinite_sequence()
print(next(gen)) #0
print(next(gen)) #1


# 惰性计算:处理[需要部分]的流式场景
def fib_seq():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

fib = fib_seq()
for _ in range(10):
    print(next(fib))
    
# 逐行处理大文件，避免将整个文件加载到内存
def read_large_file(file_path):
    with open(file_path,'r') as file:
        for line in file:
            yield line.strip()

for line in read_large_file('test.txt'):
    print(line)

