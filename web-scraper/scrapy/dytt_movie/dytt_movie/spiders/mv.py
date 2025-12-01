import scrapy

from dytt_movie.items import DyttMovieItem

class MvSpider(scrapy.Spider):
    name = 'mv'
    # 因为第二页访问的是区别于第一页的另一个网址,domains要大些,所以我们经常写域名(范围大些)
    allowed_domains = ['www.dytt8.net']
    start_urls = ['https://www.dytt8.net/html/gndy/china/index.html']

    def parse(self, response):
        # print("hello xiaoawei")
        # 获取第一页的名单和第二页对应的图片地址
        # //div[@class="co_content8"]//td[2]//a[2]/@href
        a_list=response.xpath('//div[@class="co_content8"]//td[2]//a[2]')

        for a in a_list:
            name=a.xpath("./text()").extract_first()
            href=a.xpath("./@href").extract_first()
            # print(name,href)
            # 第二页的网页连接需要拼接
            url='https://www.dytt8.net'+href
            # print(url)
            # 对第二页的链接发起请求
            yield scrapy.Request(url=url,callback=self.parse_plus,meta={"name":name})


    def parse_plus(self,response):
        # 可能因为不识别span标签导致读取到None,所以如果拿不到数据就得检查xpath语法
        src=response.xpath("//div[@id='Zoom']//img/@src").extract_first()
        name=response.meta["name"]
        movie=DyttMovieItem(name=name,src=src)
        yield movie