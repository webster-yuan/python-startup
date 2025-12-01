import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from dushu.items import DushuItem

class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1188_1.html']
    # 避免第一页的信息并没有放进去,如果只有1188结尾,不符合下面正则表达式需求,会忽略第一页的信息

    rules = (
        Rule(LinkExtractor( allow=r'/book/1188_\d+\.html'), #采用正则表达式获取有规律的网页连接
                            callback='parse_item',
                            follow=False),#为TRUE代表支持连页下载,一直到把所有的页都下载下来再停止
    )

    def parse_item(self, response):
        # 想获取图书名字和图片地址
        # // div[@class ='bookslist'] // a // img / @ data-original
        img_list=response.xpath("// div[@class ='bookslist'] // a // img ")
        for img in img_list:
            name=img.xpath('./@alt').extract_first()
            src=('./@data-original')
            book=DushuItem(name=name,src=src)
            yield book
