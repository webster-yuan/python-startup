import scrapy


class ChSpider(scrapy.Spider):
    name = 'ch'
    allowed_domains = ['car.autohome.com.cn/price/brand-15.html']
    # 如果是.html结尾的,后面不加/
    start_urls = ['https://car.autohome.com.cn/price/brand-15.html']

    def parse(self, response):
        print('#########################################')
        # print('hello xioaawei')
        # 宝马三系
        # ret=response.xpath("//div[@class='list-cont-main']/div[@id='s66']/a")
        # print(ret.extract())

        # 系列
        ret_list=response.xpath("//div[@class='main-title']/a/text()")
        prict_list=response.xpath("//div[@class='main-lever-right']//span/span/text()")
        for i in range(len(ret_list)):
            # print(ret_list[i]) # 获取标签
            print(ret_list[i].extract(),":",prict_list[i].extract()) # 获取标签中的data值

        print("##########################################")