# 双端队列，左右pop append都是O(1)
from collections import deque

from Tools.scripts.pep384_macrocheck import dprint

dq = deque(maxlen=3)
dq.append(5)
print(dq)  # deque([5], maxlen=3)
dq.extend([1, 2, 3])
dq.append(4)  # 自动挤掉 1 → deque([2, 3, 4], maxlen=3)
print(dq)  # deque([2, 3, 4], maxlen=3)
