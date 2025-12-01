import requests

url='https://www.baidu.com/s?'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
data={
    'wd':'赵今麦'
}
# params是参数,不需要urlencoding()编码
# kwargs:字典
response=requests.get(url=url,params=data,headers=headers)
content=response.text
print(content)

# 不需要请求对象的定制
# 请求资源路径中的?可以不加
# 因为requests专门属于用于爬虫,所以封装的比较好