# threading简单使用

import threading
import time

import requests


def fetch(url: str):
    start = time.time()
    response = requests.get(url, timeout=2)
    print(f"{threading.current_thread().name}  {len(response.content)}  bytes  {time.time() - start:.2f}s")


if __name__ == '__main__':
    urls = ["https://www.baidu.com"] * 5
    threads = [threading.Thread(target=fetch, args=(u,)) for u in urls]
    # 改线程名字，默认是Thread-n
    for i, t in enumerate(threads):
        t.name = f"Worker-{i}"

    for t in threads:
        t.start()

    # 主线程应该等待子线程，直接退出会导致子线程被强制终止
    for t in threads:
        t.join()  # join需要等待start，先join后start会导致死锁
