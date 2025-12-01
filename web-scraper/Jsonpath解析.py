# 只能解析本地json文件
# https://blog.csdn.net/weixin_42616506/article/details/125562884
# 连接是jsonpath与xpath的语法区别,下面是语句使用:https://blog.csdn.net/qq_36595013/article/details/109455924

# 使用jspath解析淘票票,获取所有的城市信息

import urllib.request
# 鼠标放在城市列表那里,自动跳出城市信息,在响应中看json数据信息
url='https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1674785465641_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'
headers={
    # ':authority':' dianying.taobao.com',
    # ':method':' GET',
    # ':path':' /cityAction.json?activityId&_ksTS=1674785465641_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
    # ':scheme':' https',
    'accept':' text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding':' gzip, deflate, br',
    'accept-language':' zh-CN,zh;q=0.9',
    'bx-v':' 2.2.3',
    'cookie':' t=bae132bce8f06bb45212a23869ae5909; cookie2=1416bbbedb1303615ed0325806b7c58d; v=0; _tb_token_=5d1a3e179beb1; cna=TRxaHPA1LD4CATwWd6+vM+fu; xlly_s=1; tb_city=110100; tb_cityName="sbG+qQ=="; tfstk=czjVBVjyUoEV7JWT93xNzBMWJZAAa9AMO0Jeo5rmSFG-1z8DTsYr6L2qlLJZUfYc.; l=fBggqIo7T07mGEXFBO5Bnurza77T0Idb8sPzaNbMiIEGa6t1TE3JKNCenngJ7dtjgTfbeetz_ANlDdeezQUd_giMW_N-1NKcJYp6-bpU-L5..; isg=BNDQi6f4h4C01FuEVNq8i0LJoR4imbTj4S48aMqgBytsBXGvcqwlcwR73c3l1Wy7',
    # 注意格式替换时出现的误处理
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua':' "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile':' ?0',
    'sec-ch-ua-platform':' "Windows"',
    'sec-fetch-dest':' empty',
    'sec-fetch-mode':' cors',
    'sec-fetch-site':' same-origin',
    'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-requested-with':' XMLHttpRequest',
}
request=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
# print(content)
# 去掉不需要的开头和结尾的 json109(data);,使用切割split()
content=content.split('(')[1].split(')')[0]
# print(content)
with open('淘票票城市信息.json','w',encoding='utf-8') as fp:
    fp.write(content)

import json
import jsonpath
# 只想要文件中的regionname
obj=json.load(open('淘票票城市信息.json','r',encoding='utf-8'))
city_list=jsonpath.jsonpath(obj,'$..regionName')
print(city_list)