
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import  Service

path='chromedriver.exe'
s=Service(path)
driver=webdriver.Chrome(service=s)

url='https://www.baidu.com/'
driver.get(url)

input=driver.find_element(By.ID,'su')
# 获取标签属性
print(input.get_attribute('class'))
# 获取标签的名字
print(input.tag_name)
# 获取元素文本
a=driver.find_element(By.LINK_TEXT,'视频')
print(a.text)