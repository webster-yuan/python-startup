import urllib.request

#构建url
url="http://www.baidu.com"
#根据url模拟浏览器发送request,得到返回的response
response=urllib.request.urlopen(url)
# read()是按照字节序列读取的,我们要把他解码才能看懂
content=response.read().decode('utf-8')
print(content)
