# 分页 REST API —— 惰性拉取，边用边算
import requests


def fetch_users(page_size=10):
    """GitHub /users 接口，一页一页拉，生成器惰性产出"""
    url = 'https://api.github.com/users'
    since = 0
    while True:
        params = {'since': since, 'per_page': page_size}
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        users = resp.json()
        if not users:
            return

        for user in users:
            yield user['login']

        since = users[-1]['id']


def longest_name(gen, k=5):
    """把生成器里的名字按长度取前 k 个，全程不占完整列表"""
    from heapq import nlargest
    # nlargest 是heapq（Python 内置的堆排序模块）中用于从可迭代对象中快速提取前n个最大的元素
    # key 指定排序的 依据（键函数）
    return nlargest(k, gen, key=len)


if __name__ == '__main__':
    print(longest_name(fetch_users(), 3))
