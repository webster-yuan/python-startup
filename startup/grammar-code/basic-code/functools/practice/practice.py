from functools import lru_cache, partial

import requests


@lru_cache(maxsize=32)
def fetch(request_url, timeout):
    return requests.get(request_url, timeout=timeout).text


get = partial(fetch, timeout=3)

if __name__ == '__main__':
    for url in ['https://httpbin.org/uuid'] * 5:
        print(len(get(url)))  # 首次请求网络，后 4 次直接缓存
