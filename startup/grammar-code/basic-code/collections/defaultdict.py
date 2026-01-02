from collections import defaultdict

# 直接append空的就行，免写「setdefault」
d = defaultdict(list)
for k, v in [('red', 1), ('blue', 2), ('green', 3)]:
    d[k].append(v)  # 直接 append，无需判断 key 是否存在

print(d)
# defaultdict(<class 'list'>, {'red': [1], 'blue': [2], 'green': [3]})
