
# 爬取京东信息,秒杀信息是不给你的,校验你是模拟浏览器不是真实的浏览器,设置一定的反爬机制,不给你相关信息
# 所以使用Selenium驱动真正的浏览器访问
# 安装Chrome浏览器的驱动程序:https://chromedriver.storage.googleapis.com/index.html?path=109.0.5414.74/
# 安装selenium
import  urllib.request
url="https://www.jd.com/"
response=urllib.request.urlopen(url)
content=response.read().decode('utf-8')
print(content)