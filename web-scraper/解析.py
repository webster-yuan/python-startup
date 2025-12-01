# urllib将数据爬取下来,xpath进行解析数据(并非所有的我都想要)

# from lxml import etree
# xpath 解析1.本地文件 etree.parse2.服务器响应的数据stree.HTML()

# 获取百度一下这四个字
# (1)获取网页原码
import urllib.request
url="https://www.baidu.com"
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
# print(content)
# (2)解析往内容
from lxml import etree
tree=etree.HTML(content)
# xpath的返回值就是列表类型,如果想要内容就下标访问就行
result=tree.xpath("//input[@id='su']/@value")# 通过xpath 插件验证路径获取
print(result[0])