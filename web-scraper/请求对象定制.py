import urllib.request

#url构成:协议 主机 端口号(http:80;https:443) s(路径) 参数(wd=) 锚点#
url='https://www.baidu.com'

#打印不全是因为遇到了UA反爬,需要伪装一下自己
# response=urllib.request.urlopen(url)
# content=response.read().decode('utf-8')
# print(content)

#识别到你不是浏览器,我们需要伪装()
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
# 请求对象的定制Request
request=urllib.request.Request(url=url,headers=headers)

#urlopen方法中不能存储字典,所以headers不能传进去
response=urllib.request.urlopen(request)

content=response.read().decode('utf-8')
print(content)