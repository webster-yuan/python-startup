
# 1. 导入selenium模块
from selenium import webdriver
# 2. 创建浏览器操作对象
path='chromedriver.exe'
browser=webdriver.Chrome(path)

# 3. 访问网站
url='https://jd.com/'
browser.get(url)

content=browser.page_source
print(content)
# 发现之前不提供的秒杀信息J_seckill现在已经提供了,因为我们使用驱动浏览器获取
