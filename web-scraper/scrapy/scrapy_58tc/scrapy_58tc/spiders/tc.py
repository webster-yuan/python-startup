import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = [' https://bj.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=jianzhi_B']
    start_urls = [' https://bj.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=jianzhi_B']

    def parse(self, response):
        # print('勇士总冠军')
        #     文本信息
        # content=response.text
        #     网页二进制文件
        # content=response.body
        ret=response.xpath("//div[@id='filter']/div/a/span")[0]
        print('###################################################')
        print(ret.extract())