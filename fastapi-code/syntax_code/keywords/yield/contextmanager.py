from contextlib import contextmanager


@contextmanager
def file_opener(filename:str, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()


with file_opener("data.txt", "w") as f:
    print(f.read())  # 配合着上下文管理器让文件自动关闭
