#post请求调用百度翻译

import urllib.request
import urllib.parse
#这个每个词的都不同,都得自己在网页中找,具体还不太了解
base_url="https://fanyi.baidu.com/sug"
data={
    'kw':'雄鹰'
}
# 每个post请求的参数,不许要进行编码
# 并且编码之后还得转化为字节序给到对端(encode)
new_data=urllib.parse.urlencode(data).encode('utf-8')

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

# post方法,kw不能放在url中,应该编码并且放在请求定制中
request=urllib.request.Request(url=base_url,data=new_data,headers=headers)
# 模拟浏览器向服务器发起请求
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')

#print(content)
#得到一个json字符串{"errno":0,"data":[{"k":"\u96c4\u9e70","v":"lanneret; tercel; tiercel"}]}

#字符串->json对象
import json
obj=json.loads(content)
print(obj)
#{'errno': 0, 'data': [{'k': '雄鹰', 'v': 'lanneret; tercel; tiercel'}]}