# 无界面浏览器Chrome handless
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # 添加chrome浏览器的文件路径
    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path

    browser = webdriver.Chrome(options=chrome_options)
    return browser
    # 以上代码是写死的,所以可以封装为一个函数

browser=share_browser()
url='https://www.baidu.com/'
browser.get(url)
browser.save_screenshot('baidu.png')