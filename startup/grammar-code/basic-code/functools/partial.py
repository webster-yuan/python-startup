# 提前绑定参数，生成「简化签名」的新函数
import json
from functools import partial

dump = partial(json.dumps, ensure_ascii='utf-8', indent=4)

if __name__ == '__main__':
    data = {"name": "en", "age": 20}
    print(dump(data))

# {
#     "name": "en",
#     "age": 20
# }
