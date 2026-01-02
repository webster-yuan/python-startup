# yield使用场景一：十多个G的nginx日志读取，流式读取+统计
# du -h xxx.txt 查看下读取文件的磁盘占用大小
# du命令：disk usage
# 若参数是文件：直接返回该文件的磁盘占用量；
# 若参数是目录：递归统计该目录下所有文件和子目录的总磁盘占用量。
# -h 是 human-readable 的缩写，作用是 以人类易读的单位显示磁盘大小

# htop 实时、动态地展示系统中所有运行的进程及其资源占用情况

import gzip


def iter_log(file_path):
    """支持 .gz 和普通文本，返回生成器，内存 O(1)"""
    # open_fn本身不是函数，而是保存了函数内存地址的变量
    open_fn = gzip.open if file_path.endswith(".gz") else open
    # with语句的核心作用是上下文管理，它要求后面跟随的对象必须实现「上下文管理协议」（即包含__enter__()和__exit__()两个特殊方法）
    # open_fn 会返回_io.TextIOWrapper类型对象，with将文件句柄赋值给到f
    with open_fn(file_path, 'rt', encoding="utf-8") as f:  # r:只读 t:文本格式
        # 遍历文件对象，是因为文件对象也是可迭代对象，支持逐行遍历，避免一次性加载进入内存，内存O(1)
        for line in f:
            yield line


def top_ip(log_path, n=10):
    from collections import Counter
    c = Counter()
    for line in iter_log(log_path):
        # 简单拆分，取第一个字段当 IP
        ip = line.split()[0]
        c[ip] += 1
    return c.most_common(n)


if __name__ == '__main__':
    # 把路径换成你自己的日志
    print(top_ip('/tmp/access.log', 5))
