from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        分析 k 和结果 res 的关系，当 k 越大时，即子数组的个数越多时，最大子数组和的最小值一定是越小的；
        并且可以分析出搜索区间为 [max(nums), sum(nums)]，因此联想到使用二分法确定答案；
        二分查找的目标是找到那个 最小的最大子数组和；
        用 mid 表示当前假设的最大子数组和上限，那么问题就转化为：
        在每个子数组和都 ≤ mid 的前提下，是否可以把数组切分成 ≤ k 个子数组；
        如果可以，说明 mid 仍然偏大，可以尝试继续减小，因此记录答案并令 right = mid - 1。
        """
        left, right = max(nums), sum(nums)
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2
            if self.sub_func(nums, mid, k):
                # 可以再将mid减少，求较小值
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans

    @classmethod
    def sub_func(cls, nums: List[int], mid: int, k: int) -> bool:
        """
        是否能在 每个子数组和 ≤ mid 的前提下，把数组分成 ≤ k 段
        """
        sub_arr_count, cur_sum = 1, 0
        for num in nums:
            if cur_sum + num > mid:
                sub_arr_count += 1
                cur_sum = num
            else:
                cur_sum += num

        return sub_arr_count <= k


if __name__ == '__main__':
    s = Solution()
    print(s.splitArray([7, 2, 5, 10, 8], 2))
