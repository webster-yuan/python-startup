import requests

url="https://www.baidu.com/"
response=requests.get(url=url)
# Response类型
print(type(response))
#   6个属性
# 设置响应的编码格式
response.encoding='utf-8'
# 以字符串形式返回网页的原码
print(response.text)
# 返回url地址
print(response.url)
# 返回二进制的数据
print(response.content)
# 返回响应报头
print(response.headers)
# 获取状态码
print(response.status_code)