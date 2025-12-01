# import urllib.parse
# data={
#     'wd':'赵今麦',
#     'sex':'男',
#     'location':'辽宁省沈阳市'
# }
# #wd=%E8%B5%B5%E4%BB%8A%E9%BA%A6&sex=%E7%94%B7&location=%E8%BE%BD%E5%AE%81%E7%9C%81%E6%B2%88%E9%98%B3%E5%B8%82
# # 实现字典中的自动拼接和Unicode转换
# a=urllib.parse.urlencode(data)
# print(a)


import urllib.request
import urllib.parse

base_url="https://www.baidu.com/s?"
data={
    'wd':'赵今麦',
    'sex':'女',
    'location':'辽宁省沈阳市'
}
unicode_data=urllib.parse.urlencode(data)

url=base_url+unicode_data

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
new_url=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(new_url)
content=response.read().decode('utf-8')
print(content)
# print(url)