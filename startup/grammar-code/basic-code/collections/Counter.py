from collections import Counter

colors = ['red', 'blue', 'red', 'green', 'blue', 'red']
c = Counter(colors)
# most_common 函数返回个数最多的n个元素，以及次数
print(c.most_common(1))  # [('red', 3)]
print(c.most_common(2))  # [('red', 3), ('blue', 2)]
