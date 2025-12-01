
# 第一页:https://sc.chinaz.com/tupian/renwutupian.html

# 第二页:https://sc.chinaz.com/tupian/renwutupian_2.html
# 第三页:https://sc.chinaz.com/tupian/renwutupian_3.html

# 除了第一页,其他都是:https://sc.chinaz.com/tupian/renwutupian_+page.html

import urllib.request
from lxml import etree

def create_request(page):
    if page==1:
        url='https://sc.chinaz.com/tupian/renwutupian.html'
    else:
        url='https://sc.chinaz.com/tupian/renwutupian_'
        url=url+str(page)+'.html'
    # print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        # 探寻懒加载问题错误过程,以为是报头没给够是另一种反爬
        # 'Accept-Ranges': ' bytes',
        # 'Age': ' 1',
        # 'Cache-Control': ' max-age=2592000',
        # 'Content-Length': ' 24542',
        # 'Content-Type': ' image/jpeg',
        # 'Date: Thu, 26 Jan 2023 13:45': '10 GMT',
        # 'ETag: "284721988ea5d81': '0"',
        # 'Expires: Sat, 11 Feb 2023 15:19': '10 GMT',
        # 'Last-Modified: Mon, 01 Aug 2022 10:08': '06 GMT',
        # 'Server': ' nginx',
        # 'X-Frame-Options': ' SAMEORIGIN',
        # 'X-Powered-By': ' ASP.NET',
        # 'X-Via: 1.1 nxian117:3 (Cdn Cache Server V2.0), 1.1 PS-000-01k0g16': '6 (Cdn Cache Server V2.0)',
        # 'X-Ws-Request-Id': ' 63d283e6_PS-000-01k0g16_2578-64279',
    }
    request=urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content

def parse_data(page,content):
    # 通过网页原码获得每一页的图片地址--xpath
    # urllib.request.urlretrieve('图片地址','自己起的名字')
    tree=etree.HTML(content)

    ret_name_list=tree.xpath("//div[@class='container']//img/@alt")
    ret_src_list=tree.xpath("//div[@class='container']//img/@data-original")
    # print(ret_src_list[0])

    # 一般涉及图片的网站都会进行懒加载,如果有做如下处理即可
    # 但是就上述处理测试时没有问题,相反,做以下操作后反而会出现问题,我在测试时是没有的:40 40
    # ret_src_list=tree.xpath("//div[@class='container']//img/@src2")
    # print(len(ret_src_list),len(ret_name_list))# 0 40

    for i in range(len(ret_src_list)):
        name=ret_name_list[i]
        src=ret_src_list[i]
        # print(name,src)
        url='https:'+src
        urllib.request.urlretrieve(url=url,filename='./站长素材获取图片/'+name+'.jpg')

if __name__ == '__main__':
    start_page=int(input('请输入起始页码#'))
    end_page=int(input('请输入中止页码'))

    for page in range(start_page,end_page+1):
        #   定制请求对象
        request=create_request(page)
        #   获取网页原码
        content=get_content(request)
        parse_data(page,content)