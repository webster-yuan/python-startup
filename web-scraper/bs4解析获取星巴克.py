
import urllib.request
def get_url(jpg_th):
    # print(jpg_th)
    base_url=str(jpg_th).split('(')[1].split(')')[0][1:-1]#采用切片的方式去掉前后的""
    url='https://www.starbucks.com.cn'+base_url
    # print(url)
    return url

if __name__ == '__main__':
    url='https://www.starbucks.com.cn/menu/'
    response=urllib.request.urlopen(url)
    content=response.read().decode('utf-8')
    # print(content)
    from bs4 import BeautifulSoup
    soup=BeautifulSoup(content,'lxml')
    # xpath://ul[@class='grid padded-3 product']//strong/text()
    # bs4:
    name_list=soup.select('ul[class="grid padded-3 product"] strong')
    # //ul[@class='grid padded-3 product']//a/div[@style]
    jpg_list=soup.select('ul[class="grid padded-3 product"] a>div[style]')
    # print(jpg_list[9])

    # for name in name_list:
    #     print(name.string)
    sets = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
    for i in range(len(jpg_list)):
        url=get_url(jpg_list[i])
        name=name_list[i].get_text()
        for char in name:
            if char in sets:
                name=name.replace(char,'')
        urllib.request.urlretrieve(url=url,filename='./星巴克菜单/'+str(name)+'.jpg')

# https://www.starbucks.com.cn/images/products/affogato.jpg