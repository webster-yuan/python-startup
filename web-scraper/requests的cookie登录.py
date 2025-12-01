# 隐藏域和验证码问题

import requests
# 登录页面的url地址(登录页面)
url='https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

response=requests.get(url,headers=headers)
content=response.text
# print(content)

#   通过解析获取到的网页原码,获取隐藏的登录信息:__VIEWSTATE   __VIEWSTATEGENERATOR
from bs4 import BeautifulSoup
soup=BeautifulSoup(content,'lxml')
# id获取用#
viewstate=soup.select('#__VIEWSTATE')[0].attrs.get('value')
viewstategenerator=soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

#   获取验证码图片,每次访问这个网址得到的图片都不一样
ret=soup.select('#imgCode')[0].attrs.get('src')
ret_url='https://so.gushiwen.cn'+ret
# print(ret_url)

#   下载到本地,然后再在控制台输入
# 使用request内置的session接口,保证了这是一次请求,一个对象,才保证了获取相同的验证码
# 否则采用其他方式获取验证码图片是两次请求,两个验证码
session=requests.session()
# 获取验证码url内容
response_code=session.get(ret_url)
# 因为我们使用的是图片的下载，需要使用二进制数据（所以不用text,采用content）
content_code=response_code.content
# wb的形式将二进制数据写入到文件
with open('code.jpg','wb') as fp:
    fp.write(content_code)

code_name=input('请输入验证码#')
email=input('请输入你的账号#')
pwd=input('请输入你的账号密码#')
# 填充登录信息
# 抓取登录信息接口(可以输入一个错的密码,他也会暴露出接口)
url_post='https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

data_post={
    '__VIEWSTATE':viewstate,
    '__VIEWSTATEGENERATOR':viewstategenerator,
    'from':"http://so.gushiwen.cn/user/collect.aspx",
    'email':email,
    'pwd':pwd,
    'code':code_name,
    'denglu': '登录'
}

response_post=session.post(url=url,headers=headers,data=data_post)
content_post=response_post.text
with open('gushiwen.html','w',encoding='utf-8') as fp:
    fp.write(content_post)

# 键盘输入验证码很不方便,所以我们需要验证码解析平台,例如超级鹰