from selenium import webdriver
# 解决AttributeError: 'WebDriver' object has no attribute 'find_element_by_id'
# https://blog.csdn.net/qq_43985140/article/details/126847603
from selenium.webdriver.common.by import By
# 解决DeprecationWarning: executable_path has been deprecated, please pass in a Service object
# https://blog.csdn.net/qq_43281203/article/details/127956323
from selenium.webdriver.chrome.service import Service

path='chromedriver.exe'
# browser=webdriver.Chrome(path)

# 尝试传参
s = Service(path)
driver = webdriver.Chrome(service=s)

url='https://www.baidu.com/'

driver.get(url)
# browser.get(url)

    # 1. 根据id来找到对象
# # button=browser.find_element_by_id('su') 这样写已经不行了
# button = driver.find_element(By.ID,'su')
# print(button)
    # 2. 根据标签属性的属性值获取对象
# # button=driver.find_element_by_name('wd')  这样写已经不行了
# button =driver.find_element(By.NAME,'wd')
# print(button)
#     3. 根据xpath 语句获取对象
# button=driver.find_element(By.XPATH,'//input[@id="su"]')
# print(button)
#   4. 根据标签的名字获取对象
# button=driver.find_elements(By.TAG_NAME,'input')
# print(button)
#   5. 使用bs4的语法获取对象
button=driver.find_elements(By.CSS_SELECTOR,'#su')
print(button)
#   6.
# button =driver.find_element(By.LINK_TEXT,'视频')
# print(button)