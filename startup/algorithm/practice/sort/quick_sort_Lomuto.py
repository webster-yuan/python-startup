# “看到小的就往左放”
# 遍历一遍，把所有 ≤ pivot 的数收集到左边
# [left ... i]        → 已经整理好的：<= pivot
# [i+1 ... j-1]      → 已经看过，但 > pivot
# [j ... right-1]    → 还没处理
# [right]            → pivot

# [ <= pivot | pivot | > pivot ]
# [   空     |  1   |   全部   ]


def quick_sort(arr, left=None, right=None):
    #  初始化左右边界
    if left is None:
        left = 0

    if right is None:
        right = len(arr) - 1

    # 递归终止条件
    if left >= right:
        return

    pivot_index = partition(arr, left, right)
    quick_sort(arr, left, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, right)


def partition(arr, left, right):
    # 选择右边为基准
    pivot = arr[right]
    i = left - 1  # 负责拓展小于区间
    for j in range(left, right):  # j 负责遍历数组
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]

    return i + 1


arr = [3, 5, 6, 2, 1]
quick_sort(arr)
print(arr)
