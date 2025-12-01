import scrapy


class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['http://www.dytt8.net/']

    def parse(self, response):
        pass
