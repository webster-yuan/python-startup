# 实现思路：“左右找错的人，然后交换”
# [left]         → pivot（还没归位）
# (left, i)      → <= pivot
# (j, right)     → >= pivot
# [i, j]         → 未处理

def quick_sort(nums, left, right):
    if left >= right:
        return

    pivot = nums[left]
    i, j = left, right
    while i < j:
        # 从右边找比pivot小的数
        while i < j and nums[j] >= pivot:
            j -= 1

        # 从左边找比pivot大的数
        while i < j and nums[i] <= pivot:
            i += 1

        # 交换
        nums[i], nums[j] = nums[j], nums[i]

    nums[left] = nums[i]
    nums[i] = pivot

    quick_sort(nums, left, i - 1)
    quick_sort(nums, i + 1, right)


nums = [3, 1, 4, 1, 5, 9, 2, 6]
quick_sort(nums, 0, len(nums) - 1)
print(nums)  # [1,1,2,3,4,5,6,9]
