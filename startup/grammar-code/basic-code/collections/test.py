# 日志 Top-N + 滑动窗口均值
from collections import Counter, deque


def top_n_and_avg(lines, n=3, window=5):
    c = Counter()
    dq = deque(maxlen=window)
    for line in lines:
        ip = line.split()[0]
        c[ip] += 1
        dq.append(len(line))
        yield c.most_common(n), sum(dq) / len(dq)
