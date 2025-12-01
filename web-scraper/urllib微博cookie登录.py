# 只有登录信息之后才能获取信息
# 这是一个反扒手段
# 个人信息页面是utf-8但是报错编码错误,其实是跳转到登录页面,而登录页面不是utf-8,所以会报格式错误
# import urllib.request
#
# url='https://weibo.com/6776795609/info'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
# }
#
# request=urllib.request.Request(url=url,headers=headers)
# response=urllib.request.urlopen(request)
# #content=response.read().decode('utf-8')
# #UnicodeDecodeError: 'utf-8' codec can't decode byte 0xca in position 339: invalid continuation byte
# content=response.read().decode('gb2312')#登录页面编码格式
# with open('weibo.html','w',encoding='utf-8') as fp:
#     fp.write(content)

# 如何跳过登录页面?不成功就是提供的条件不够
# 验证:在登录好的页面中
# cookie中携带着你的登录信息,如果有登录之后的cookie就可以携带cookie进入任何页面
# referer 判断当前路径是否是从上一级来的,一般用于图片防盗链,不是的话就不让你下载
import urllib.request

url='https://weibo.com/6776795609/info'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
# }
headers={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': '''XSRF-TOKEN=Llqe10zAI_662i-J-pZA3Yhc; WBPSESS=dg5zs_KFY81p0FnDKmb34cFWEHX4o7X-tFiiWNHBaVpdDsG6KvumHno8YoDWYz_QNJV6oKbPBS9_pkXfVzeP_0OVPAsemwhBg0klZKfMUEeVeyF_m_6UzaREmT9quejK4JewHni4JyNKq9nqCdeTKy3RuS0p6dcF-6Lzy3MHyVk=; login_sid_t=973a8627c824b63dfdaea454e68f2f62; cross_origin_proto=SSL; _s_tentry=weibo.com; Apache=146211820688.11578.1674570863211; SINAGLOBAL=146211820688.11578.1674570863211; ULV=1674570863218:1:1:1:146211820688.11578.1674570863211:; wb_view_log=1536*8641.375; WBtopGlobal_register_version=2023012422; appkey=; SSOLoginState=1674571106; SUB=_2A25Oy53-DeRhGeBJ7FQW-SvKyzWIHXVtoIg2rDV8PUNbmtAKLVfRkW9NRiy_iyyMzzGZbxlzpv1-sBD0TLJ7FCtd; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5noZ5NMrB7SXXxGKxoZqxD5JpX5KzhUgL.FoqNS0qN1K-ceh.2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMcS0McS0.fSo54; ALF=1706107182; wvr=6; wb_view_log_6776795609=1536*8641.375; UOR=,,www.baidu.com; PC_TOKEN=cccffcf26f; webim_unReadCount=%7B%22time%22%3A1674571805007%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A15%2C%22msgbox%22%3A0%7D''',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
with open('weibo.html','w',encoding='utf-8') as fp:
    fp.write(content)