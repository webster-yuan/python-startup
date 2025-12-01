from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

path='chromedriver.exe'
s=Service(path)
driver=webdriver.Chrome(service=s)

url='https://www.baidu.com/'
driver.get(url)

# 根据id获取文本框
text=driver.find_element(By.ID,'kw')
text.send_keys('赵今麦')
# 获取百度一下的button按键
button=driver.find_element(By.ID,'su')

import time
time.sleep(2)
button.click()
time.sleep(2)

# 点击图片按键,通过LINK_TEXT实现定位
button =driver.find_element(By.LINK_TEXT,'图片')
button.click()
time.sleep(2)

# 返回上一步
driver.back()

# 划到底部
js_bottom='document.documentElement.scrollTop=100000'
driver.execute_script(js_bottom)
time.sleep(2)

# 点击下一页
button=driver.find_element(By.XPATH,'//a[@class="n"]')
button.click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.quit()

# 由于css渲染以及浏览器的使用,使得效率降低
# 可以使用phantomjs.exe无界面浏览器(已经停更建议使用Chrome handless在不打开浏览器的情况下完成)