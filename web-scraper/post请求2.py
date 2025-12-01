
import urllib.request
import urllib.parse

url="https://fanyi.baidu.com/v2transapi?from=en&to=zh"
data={
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'simple_means_flag': '3',
    'sign': '198772.518981',
    'token': '82c828acccd50f429c01bda6e9772493',
    'domain': 'common'
}
#       Cookie反爬
headers={
    #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Cookie':''' BIDUPSID=26FC065408715F33F7EB23F4CA458441; PSTM=1673958290; BAIDUID=26FC065408715F33D3DB8747DA4E99D7:FG=1; BAIDUID_BFESS=26FC065408715F33D3DB8747DA4E99D7:FG=1; ZFY=ywmC27ClEMzqw:AUDK9A1kCRtWryhCb0OWdCm2M8RbPE:C; __bid_n=185bfd3c0cfa906ac74207; FPTOKEN=Xk/sUAT2VjoNW52zQ9baqNXyIlnmYp7NsIZP7smvcqrqilExkqYXc4WoV8V+WKF9y463HyZaFOYpN483TfiAZOyPaBYcyosDAcjmNy2peevRXM+vKDwsVCPRvfR47rb/bpJF3kF+GP74azOLldXbEuskyh2C87QRuS42qokaNP6KaGvynA7c1SZ7Mr7OhMzc8mByFRksGGv7Vf+94MQ3ZXz9diNFl5J5B14ofNlZTpmQvH9aHJmSvjLfgv1pGqmspkqzrHhhxAUa+R1uNAQXiy84lcsOH5Bj/p0hKfod0BWd0ZdG4meRpsYVMzWmXPkS1of1eFj/E5BjaB9kreaHDKVWgv+kp8YcdZYwQ70+Ml9VeWdKIs5TZQi0dGrXOPQsZDSN5jCrrlSUkM/WnEevBQ==|mpTsCNomKa0h7RomvzZc2wbVkAAmDyOe9uQLbKavBgA=|10|194e6625fdc74e23c0f5af7fd5d0f691; BA_HECTOR=2gah8l8k8lakahagak8ga1tv1hsh9481l; BDRCVFR[shpneSZgko0]=mk3SLVN4HKm; delPer=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; image_bff_sam=1; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDRCVFR[tox4WRQ4-Km]=mk3SLVN4HKm; BDRCVFR[A24tJn4Wkd_]=mk3SLVN4HKm; ariaDefaultTheme=undefined; RT="z=1&dm=baidu.com&si=oya41huqslr&ss=ld2h7yt1&sl=6&tt=53c&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=11c1&cl=zuc&ul=3jot&hd=3jqf"; H_PS_PSSID=26350; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; APPGUIDE_10_0_2=1; FANYI_WORD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1674100908; PSINO=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1674110212; ab_sr=1.0.1_ODdjNTI2MTlhNGRjNmZjYTM3Y2MzYjQ1YmNkNmEyN2ZkNGIyNGM3Yzc0ODY5Njg0YWQyNGViMTFjMDczM2ExOTVkYmViOTI1ZjBhNzgzMzBmNTRiZjhlOTdhODJjNjUwNjkxOGZhODI5YmE4MzlmZTMxOGJkM2JiMmZmYzNiOTI5MGFiNjNlMTA2MGViNGM1NjJiZWUzNzk2MGEzYzI1NQ=='''
}
# 将data编码并转化为字节序
new_data=urllib.parse.urlencode(data).encode('utf-8')
# post方法,kw不能放在url中,应该编码并且放在请求定制中
request=urllib.request.Request(url=url,data=new_data,headers=headers)
# 模拟浏览器向服务器发起请求
response=urllib.request.urlopen(request)
content=response.read().decode('utf-8')
import json
obj=json.loads(content)
print(obj)
