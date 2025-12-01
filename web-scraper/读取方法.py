import urllib.request

url="http://www.baidu.com"

response=urllib.request.urlopen(url)
#<class 'http.client.HTTPResponse'>
print(type(response))

#read字节个数方式读取
content1=response.read(5)
#读取一行
content2=response.readline()
#读取多行
content3=response.readlines()

#返回状态码,如果是200就说明代码没问题
print(response.getcode())

#返回url地址
print(response.geturl())

#获取状态信息
print(response.getheaders())