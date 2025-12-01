# Python网页爬虫项目

这是一个全面的Python网页爬虫学习和实践项目，包含了从基础到高级的多种爬虫技术实现，涵盖了不同场景下的数据抓取方法。

## 项目功能

本项目实现了多种网页数据爬取功能，包括但不限于：

- 基础HTTP请求与响应处理
- 静态网页内容解析
- 动态网页(Ajax)数据爬取
- 表单提交与POST请求
- Cookie登录与会话维护
- 代理IP使用
- 浏览器自动化
- 大型爬虫框架应用
- 图片资源下载
- 结构化数据存储(JSON等)

## 技术栈

- **Python 3.x**：主要开发语言
- **urllib**：Python标准库，提供基础的网络请求功能
- **requests**：功能强大的HTTP库，简化API调用
- **BeautifulSoup**：HTML和XML解析库
- **lxml**：高效的XML/HTML解析器
- **Selenium**：自动化测试工具，用于模拟浏览器行为
- **Scrapy**：强大的Python爬虫框架
- **ChromeDriver**：Chrome浏览器驱动，配合Selenium使用

## 项目结构

```
web-scraper/
├── 基础请求示例/            # 各种HTTP请求方法示例
│   ├── main.py             # urllib基础使用
│   ├── requests基本使用.py  # requests库基本操作
│   ├── get请求方式urlencode().py
│   ├── post请求.py
│   └── ...
├── 解析示例/               # 数据解析相关代码
│   ├── BeautifulSoup解析.py
│   ├── Jsonpath解析.py
│   ├── 解析.py
│   └── ...
├── Selenium示例/           # 浏览器自动化示例
│   ├── Selenium.py
│   ├── Selenium使用.py
│   ├── selenium元素定位.py
│   ├── selenium元素交互.py
│   └── ...
├── Scrapy项目/             # Scrapy爬虫框架项目
│   ├── baidu/             # 百度爬虫项目
│   ├── carhome/           # 汽车之家爬虫项目
│   ├── dangdang/          # 当当网爬虫项目
│   ├── dushu/             # 读书网站爬虫项目
│   ├── dytt_movie/        # 电影天堂爬虫项目
│   └── ...
├── 实战案例/               # 实际爬虫案例
│   ├── ajax的get请求豆瓣电影.py
│   ├── ajax的post请求获取肯德基门店信息.py
│   ├── bs4解析获取星巴克.py
│   ├── 获取站长素材的图片.py
│   ├── 爬取QQ空间主页信息.py
│   └── ...
└── 数据文件/               # 爬取的结果数据
    ├── douban.json        # 豆瓣电影数据
    ├── post_kfc/          # 肯德基门店数据
    ├── 星巴克菜单/         # 星巴克产品图片
    └── ...
```

## 主要模块介绍

### 1. 基础网络请求

包含使用`urllib`和`requests`库进行HTTP请求的基本操作，如GET、POST请求，请求头设置，Cookie处理等。

### 2. 数据解析

使用`BeautifulSoup`和`lxml`等库解析HTML/XML内容，提取所需数据。

### 3. Selenium自动化

通过Selenium模拟真实浏览器行为，解决JavaScript渲染、动态加载等问题。

### 4. Scrapy框架应用

使用Scrapy框架构建完整的爬虫项目，包含多个实际案例：

- 百度搜索
- 汽车之家数据
- 当当网图书信息
- 读书网站内容
- 电影天堂资源

### 5. 反爬虫策略应对

包含代理IP使用、User-Agent轮换、Cookie处理等反爬虫技术。

## 环境要求

- Python 3.x
- 主要依赖包：
  ```
  pip install requests beautifulsoup4 lxml selenium scrapy
  ```
- Chrome浏览器及对应版本的ChromeDriver

## 使用方法

1. 安装必要的依赖包：
   ```
   pip install -r requirements.txt
   ```

2. 运行具体的爬虫脚本：
   ```
   python 文件名.py
   ```

3. 运行Scrapy项目：
   ```
   cd scrapy/项目名称
   scrapy crawl 爬虫名称
   ```

## 注意事项

1. 请遵守网站的robots.txt规则和相关法律法规
2. 合理控制爬取频率，避免对目标网站造成过大压力
3. 某些示例需要下载对应版本的ChromeDriver并放在正确位置

## 学习资源

本项目可以作为Python爬虫学习的综合示例，从基础到高级，逐步深入了解网页爬虫技术。

## 许可证

本项目仅供学习和参考使用。
        