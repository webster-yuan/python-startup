import scrapy
from dangdang.items import  DangdangItem
class DdSpider(scrapy.Spider):
    name = 'dd'
    # allowed_domains = ['http://category.dangdang.com/cp01.54.06.01.00.00.html']
    # 如果是多页下载的话是要调整这个的范围
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.54.06.01.00.00.html']

    base_url="http://category.dangdang.com/pg"
    page=1

    def parse(self, response):
        # pipeline:管道
        # items:数据结构
        # src://ul[@id='component_59']/li//img/@src,图片懒加载反爬的原因,更换
        # src://ul[@id='component_59']/li//img/@data-original
        # alt://ul[@id='component_59']/li//img/@alt
        # price://ul[@id='component_59']/li/p[@class='price']/span[@class='search_now_price']/text()
        li_list=response.xpath("//ul[@id='component_59']/li")
        for li in li_list:
            src=li.xpath(".//img/@data-original").extract_first()
            # 第一场图片是没有data-original的
            if src:
                src=src
            else:
                src=li.xpath(".//img/@src").extract_first()

            alt=li.xpath(".//img/@alt").extract_first()
            price=li.xpath("./p[@class='price']/span[@class='search_now_price']/text()").extract_first()
            # print(src,"-",alt,"-",price)
#           获取完成内容,下面需要用管道将信息保存在文件中
            book=DangdangItem(src=src,name=alt,price=price)
            yield book #return 返回值,获取一个book就交给管道保存
        # 每一页获取一个list,下一页只需要都会进行相同的操作
        # page2:http://category.dangdang.com/pg2-cp01.54.06.01.00.00.html
        # page3:http://category.dangdang.com/pg3-cp01.54.06.01.00.00.html

        if self.page<10:
            self.page=self.page+1

            url=self.base_url+str(self.page)+'-cp01.54.06.01.00.00.html'

#             怎么调用parse方法
#             Request就是scrapy的get方法
#             callback就是你要调用的函数,不需要加()
            yield scrapy.Request(url=url,callback=self.parse)
