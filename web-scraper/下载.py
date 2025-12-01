import urllib.request
#下载网页
# url_page="http://www.baidu.com"
# urllib.request.urlretrieve(url_page,filename="baidu.html")

#下载图片
# url_img="https://img0.baidu.com/it/u=3171633608,3901752065&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=667"
# urllib.request.urlretrieve(url_img,filename="赵今麦.jpg")
#下载视频
url_video="https://vd2.bdstatic.com/mda-pah55vq7hzqpx257/sc/cae_h264/1674013416208139453/mda-pah55vq7hzqpx257.mp4?v_from_s=hkapp-haokan-hbe&auth_key=1674097316-0-0-997e3f9d965b6083142cdf5f7a314ebb&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=1916012906&vid=3790631280984655793&abtest=&klogid=1916012906"
urllib.request.urlretrieve(url_video,filename="勇士白宫.mp4")
# print(resonse.getcode())