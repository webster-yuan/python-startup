# 获取豆瓣电影动作片的排行榜前20名(第一页)的电影信息
import urllib.request

url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

# (1)定制请求
request=urllib.request.Request(url=url,headers=headers)
# (2)获取相应
response=urllib.request.urlopen(request)
# (3)获取内容并写入
content=response.read().decode('utf-8')

# open 方法默认情况下使用的是gbk的编码,如果我们想要保存汉字就需要转化为utf-8的编码
# encoding='utf-8'
fp=open('douban.json','w',encoding='utf-8')
fp.write(content)