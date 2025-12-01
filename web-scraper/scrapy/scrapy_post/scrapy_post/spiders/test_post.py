import scrapy
import json

class TestPostSpider(scrapy.Spider):
    name = 'test_post'
    allowed_domains = ['www.fanyi.baidu.com/sug']
        # post请求如果没有向上传递参数就没有意义
        # 因为参数的变化所以网页起始地址start_url就没用了,
        # 而函数parse就是处理start_url的,所以也就没有用了
    # start_urls = ['http://www.fanyi.baidu.com/']
    #
    # def parse(self, response):
    #     pass
    def start_requests(self):
        url="https://fanyi.baidu.com/sug"
        data={
            'kw':'final'
        }
        yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse_second)

    def parse_second(self ,response):
        content=response.text
        # print(content)

        obj=json.loads(content,encoding='utf-8')
        print(obj)
        # E:\python爬虫程序\python\pythonProject\scrapy\scrapy_post\scrapy_post\spiders>scrapy crawl test_post
        # {'errno': 0, 'data': [{'k': 'final', 'v': 'adj. 最后的，最终的; 决定性的; 不可更改的 n. 决赛; 结局; 期末考试; 〈口〉（报纸的'}, {'k': 'FINAL', 'v': 'abbr. financial analysis language 财政分析语言'}, {'k': 'finale', 'v': 'n. [乐]终曲; 结局，大团圆; 最后一场，最后乐章; 尾声'},
        # {'k': 'Finale', 'v': '[人名] 菲纳利; [地名] [意大利] 菲纳莱'}, {'k': 'finals', 'v': '[体]决定性的比赛'}]}