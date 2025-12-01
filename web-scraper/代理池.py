
proxies_pool=[
    {'http':'117.114.149.66:55443'},
    {'http':'27.42.168.46:55481'}
]
import random
proxies=random.choice(proxies_pool)

# 以后和之前的代理代码一致