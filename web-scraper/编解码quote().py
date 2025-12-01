# 多语言混合存在乱码的行为
# 所以出现了Unicode编码
#quote方法就是将汉字转化为unicode编码

import urllib.request
import urllib.parse
url="https://www.baidu.com/s?wd="

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
#   将搜索汉字转化为Unicode编码
name= urllib.parse.quote('赵今麦')
# print(name)
url=url+name
#   应对UA反爬的伪装
request=urllib.request.Request(url=url ,headers=headers)
#   发送请求
response=urllib.request.urlopen(request)
#   解析数据
content=response.read().decode('utf-8')
print(content)
# print(url)