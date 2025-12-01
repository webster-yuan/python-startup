# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class DushuPipeline:
    def open_spider(self,spider):
        self.fp=open('book.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item
    def close_spider(self,spider):
        self.fp.close()

# 加载settings文件
from scrapy.utils.project import get_project_settings

class MysqlPipeline:
    def open_spider(self,spider):
        # DB_HOST='101.43.176.238'
        # DB_PORT=3306
        # DB_USER='root'
        # DB_PASSWORD='yuanwei0710@honey.666'
        # DB_NAME='spider01'
        # DB_CHARSET='utf-8'
        settings=get_project_settings()
        self.host=settings['DB_HOST']
        self.port=settings['DB_PORT']
        self.user=settings['DB_USER']
        self.password=settings['DB_PASSWORD']
        self.name=settings['DB_NAME']
        self.charset=settings['DB_CHARSET']

        self.connect()

    def connect(self):
        self.conn=pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.name,
            charset=self.charset
        )
        self.cursor=self.conn.cursor()

    def process_item(self, item, spider):
        sql='insert into book (name,src) values("{}","{}")'.format(item["name"],item["src"])

        self.cursor.execute(sql)#执行
        self.conn.commit()#提交

        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()