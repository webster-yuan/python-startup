#下载豆瓣电影前10页的数据

# 第一页url page=1
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=0&limit=20

# 第二页url page=2
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=20&limit=20

# 所以start=(page-1)*limit
import urllib.request
import urllib.parse
def create_request(page):
    base_url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    # get方法只需要将data拼接到url中即可
    data={
        'start':(page-1)*20,
        'limit':20
    }
    union_data=urllib.parse.urlencode(data)
    url=base_url+union_data
    # print(url)

    request=urllib.request.Request(url=url,headers=headers)
    return request

def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content

def download_data(content,page):
    fp=open('douban_'+str(page)+'.json','w',encoding='utf-8')
    fp.write(content)

if __name__ == '__main__':
    start_page=int(input('请输入想要获取的起始页码#'))
    end_page=int(input('请输入想要获取的结束页码#'))
    # 每一页都需要进行一下三个步骤
    for page in range(start_page,end_page+1):
        # 定制请求对象
        request = create_request(page)
        # 获取内容
        content = get_content(request)
        # 下载数据
        download_data(content,page)