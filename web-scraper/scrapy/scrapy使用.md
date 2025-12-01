* scrapy基本操作

  ![image-20230131093730381](https://image-1309381344.cos.ap-nanjing.myqcloud.com/img/image-20230131093730381.png)

* 自己操作实例:

![image-20230131093843346](https://image-1309381344.cos.ap-nanjing.myqcloud.com/img/image-20230131093843346.png)

* scrapy crawl baidu

![image-20230131093943279](https://image-1309381344.cos.ap-nanjing.myqcloud.com/img/image-20230131093943279.png)

* robots协议

  ![image-20230131094014213](https://image-1309381344.cos.ap-nanjing.myqcloud.com/img/image-20230131094014213.png)

![image-20230131095625207](https://image-1309381344.cos.ap-nanjing.myqcloud.com/img/image-20230131095625207.png)

![image-20230131105730564](https://image-1309381344.cos.ap-nanjing.myqcloud.com/img/image-20230131105730564.png)

##### scrapy shell

```shell
C:\Users\小可爱>scrapy shell www.baidu.com
```

![image-20230131110938686](https://image-1309381344.cos.ap-nanjing.myqcloud.com/img/image-20230131110938686.png)

![image-20230131110824158](https://image-1309381344.cos.ap-nanjing.myqcloud.com/img/image-20230131110824158.png)

##### scrapy连接提取器

使用scrapy shell:

`C:\Users\小可爱>scrapy shell https://www.dushu.com/book/1188.html`

![image-20230131214720443](https://image-1309381344.cos.ap-nanjing.myqcloud.com/img/image-20230131214720443.png)

获取到如上连接只有页码数不同的网页地址.

#### CrawlSpider连接提取器

![image-20230131215948829](https://image-1309381344.cos.ap-nanjing.myqcloud.com/img/image-20230131215948829.png)

`mysql> GRANT ALL PRIVILEGES ON spider01 to 'xiaoawei' @'%' IDENTIFIED BY 'xiaoawei0828@HONEY.666' WITH GRANT OPTION;`