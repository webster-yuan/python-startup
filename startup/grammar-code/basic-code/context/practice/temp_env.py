import pathlib
from contextlib import contextmanager
import os


@contextmanager
def temp_env(**kwargs):
    backup = {k: os.environ.get(k) for k in kwargs}
    os.environ.update(kwargs)
    try:
        yield
    except Exception as e:
        print(e)
    finally:
        for k, v in backup.items():
            if v is None:
                os.environ.pop(k)
            else:
                os.environ[k] = v


@contextmanager
def chdir(path):
    """临时切换工作目录"""
    old_path = pathlib.Path.cwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(old_path)


if __name__ == '__main__':
    print("before:", os.getcwd(), os.getenv('MY_ENV'))
    with temp_env(MY_ENV='MY_ENV'), chdir("/tmp"):
        print("inside:", os.getcwd(), os.getenv('MY_ENV'))
        
    print("after:", os.getcwd(), os.getenv('MY_ENV'))
