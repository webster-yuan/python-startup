
from bs4 import BeautifulSoup
# 解析本地文件理解基础语法
soup=BeautifulSoup(open('bs4基本使用.html','r',encoding='utf-8'),'lxml')
# 根据标签名查找节点,找到的是第一个符合条件的数据
# print(soup.a)
# # 获取标签的属性和属性值
# print(soup.a.attrs)
#
# # bs4的一些函数
# # (1)find,返回标签对象
# print(soup.find('a'))
# print(soup.find('a',title='6666'))
# print(soup.find('a',class_='a1'))
# (2)find_all 返回一个列表包含所有的a标签
    # 如何向获得的是多个标签的数据,需要在参数中添加的是列表的数据
# print(soup.find_all(['a','span']))
#
# print(soup.find_all('li'),limit=1)#前几个
# (3)select 返回的是一个列表包含多个数据
# print(soup.select('a'))
# 可以通过.代表class,这样的操作叫做类选择器
# print(soup.select('.a1'))

# print(soup.select('#l1'))
# 属性选择器,通过属性找到对应的标签
# 查找到li 标签中有id的标签
# print(soup.select('li[id]'))

# 查找到li标签中id=l1的标签
# print(soup.select('li[id="l1"]'))

# 层级选择器
# 后代选择器:找到div下面的li
# print(soup.select('div li'))
# 子代选择器,某标签的第一级子标签
# print(soup.select('div > ul > li'))

# 节点信息]
# 获取节点内容
# select返回的是列表
# obj=soup.select('#a1')[0]
# # 如果标签对象中,只有内容,那么都可以使用
# # 如果出了内容还有标签,string 就获取不到数据,而get_text()可以获取数据
#
# print(obj.string)
# print(obj.get_text())

# 节点属性
# obj=soup.select('#p1')[0]
# print(obj.name)
# # 将属性值作为一个字典返回
# print(obj.attrs)

# 获取节点的属性
obj=soup.select('#p1')[0]
# 字典获取数据
print(obj.attrs.get('class'))