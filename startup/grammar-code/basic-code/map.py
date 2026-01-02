def map_main():
    urls = ['a.com', 'b.com', 'c.com']
    # map核心功能是将一个指定的函数，依次应用到一个或多个可迭代对象的每个元素上，
    # 返回一个迭代器（map 对象），该迭代器包含所有元素经过函数处理后的结果
    full_urls = list(map("https://".format, urls))
    print(full_urls)


map_main()
