
import urllib.request
url='https://www.baidu.com/s?wd=IP'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

request=urllib.request.Request(url=url,headers=headers)

# 代理服务器以字典形式存在
# 访问 快代理-免费代理.或者购买之后访问生成的API连接就行
# 实现使用别人的IP进行访问,避免封掉自己的IP
proxies={
    'http':'222.74.73.202:42055'
}
# 参数proxies: dict[str, str]
handler=urllib.request.ProxyHandler(proxies=proxies)
opener=urllib.request.build_opener(handler)

response=opener.open(request)
content=response.read().decode('utf-8')

with open('daili.html','w',encoding='utf-8') as fp:
    fp.write(content)