# 已排序列表的“快速插入/定位”
import bisect

scores = [10, 20, 30, 40, 50]  # 必须升序
# 查找35应该放在数组中的哪个位置
idx = bisect.bisect_left(scores, 35)
print(idx)

bisect.insort(scores, 35)  # 插入并保持有序
print(scores)  # [10, 20, 30, 35, 40, 50]
