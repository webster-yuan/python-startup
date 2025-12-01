import urllib.request

url='http://user.qzone.qq.com/3277930931/main'

headers={
# :authority: user.qzone.qq.com
# :method: GET
# :path: /3277930931/main
# :scheme: https
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# accept-encoding: gzip, deflate, br
'accept-language': 'zh-CN,zh;q=0.9',
'cookie':''' _qpsvr_localtk=0.49304944145209295; RK=K71onzCN/E; ptcz=6c802a984e940e8990e1722ebdffd77889b8c6219200e817d50b93a494218ab6; uin=o3277930931; skey=@IFgVRACfd; p_uin=o3277930931; pt4_token=N560k2mFq3uWWvecJ2muaidURP44A1ig8PSmzrGxQ0g_; p_skey=zgON2BUErMzyxSUR89sKxb2Pp3ncXH8CoCmY0qgDvdg_; Loading=Yes; qz_screen=1536x864; 3277930931_todaycount=0; 3277930931_totalcount=5913; pgv_pvid=1308979423; pgv_info=ssid=s6923071080; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=0''',
'if-modified-since': 'Tue, 24 Jan 2023 15:14:05 GMT',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'cross-site',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

request=urllib.request.Request(url=url ,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')#经查勘,页面编码是utf8
with open('qqzone.html','w',encoding='utf-8') as fp:
    fp.write(content)
