# 爬取肯德基餐厅查询信息post方法
# 在headers中出现这个:X-Requested-With: XMLHttpRequest,就是post方法

# 第一页:
# Request URL: http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 沈阳
# pid:
# pageIndex: 1
# pageSize: 10

# 第二页:
# Request URL: http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 沈阳
# pid:
# pageIndex: 2
# pageSize: 10
import urllib.request
import ssl
import urllib.parse

def create_request(page):
    base_url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data={
        'cname': '沈阳',
        'pid':'',
        'pageIndex': page,
        'pageSize': 10
    }
    new_data=urllib.parse.urlencode(data).encode('utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    request=urllib.request.Request(url=base_url,headers=headers,data=new_data)
    # print(request)
    return request


def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content


def download_data(content,page):
    with open('E:\python爬虫程序\python\pythonProject\post_kfc\kfc_'+str(page)+'.json','w',encoding='utf-8') as fp:
        fp.write(content)

if __name__ == '__main__':
    start_page=int(input('请输入起始页数#'))
    end_page=int(input('请输入终止页数#'))
    for page in range(start_page,end_page+1):
        # 定制对象
        request=create_request(page)
        # 返回信息
        content=get_content(request)
        # 下载
        download_data(content,page)