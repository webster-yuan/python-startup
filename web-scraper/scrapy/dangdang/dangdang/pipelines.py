# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import urllib.request

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DangdangPipeline:
    def open_spider(self, spider):
        self.fp=open('book.json','a',encoding='utf-8')

    def process_item(self, item, spider):
        # 对文件操作过于频繁,每传递一个对象就要打开一次文件
        # 所以定义另外两个函数控制打开还是关闭文件
        # # 要使用管道,就必须在setting中开启管道
        # # w会对文件进行覆盖,所以使用a 追加
        # with open('book.json','a',encoding='utf-8') as fp:
        #     fp.write(str(item))
        self.fp.write(str(item))
        return item

    def close_spider(self, spider):
        self.fp.close()
# 多条管道开启
# 定义管道类
# 在settings中开启管道
class DangDangDownLoad():
    def process_item(self,item,spider):
        url='https:'+item.get('src')
        filename='./books/'+item.get('name')+'-'+item.get('price')+'.jpg'
        urllib.request.urlretrieve(url=url,filename=filename)

        return item