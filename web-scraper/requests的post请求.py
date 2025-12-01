# post爬取百度翻译

import requests

url='https://fanyi.baidu.com/sug'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
data={
    'kw':'eye'
}
response=requests.post(url=url,data=data,headers=headers)
content=response.text
import json
obj=json.loads(content,encoding='utf-8')
print(obj)

# post 请求不需要编解码
# 不需要请求对象定制