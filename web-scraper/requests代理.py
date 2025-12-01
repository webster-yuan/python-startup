import requests
url='https://www.sogou.com/web?'

data={
    'query':'ip'
}
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
proxy={
    'http':'121.13.252.58:41564'
}
response=requests.get(url=url,params=data,headers=headers,proxies=proxy)
response.encoding='utf-8'
content=response.text
with open('daili.html','w',encoding='utf-8') as fp:
    fp.write(content)