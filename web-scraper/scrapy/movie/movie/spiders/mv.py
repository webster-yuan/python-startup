import scrapy


class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['www.ygdy8.net']
    start_urls = ['http://www.ygdy8.net/']

    def parse(self, response):
        pass
