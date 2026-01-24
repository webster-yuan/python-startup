from typing import List


class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            other = target - num
            # T = O(n^2)
            # S = O(1)
            if other in nums[index + 1:]:  # 避免find == num，导致乌龙 T=O(n)
                # pos 从下一个元素返回，应对重复元素，因为index只会返回第一个匹配的元素
                # T=O(n)
                return [index, nums.index(other, index + 1)]

        return []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 使用哈希表
        # T = O(n)
        # S = O(n)
        seen = {}
        for index, num in enumerate(nums):
            other = target - num
            if other in seen:
                return [seen[other], index]

            seen[num] = index

        return []

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        """
        排序后数组对应的下标会发生变化，所以还是需要O(n)的空间存储原始数组元素映射原始下标
        倒不如直接使用哈希表
        """
        # 值+原始下标
        arr = [(v, i) for i, v in enumerate(nums)]
        arr.sort()  # 按值排序 T = O(n * log n)

        left, right = 0, len(arr) - 1
        while left < right:
            s = arr[left][0] + arr[right][0]
            if s == target:
                # 注意返回原始下标
                return [arr[left][1], arr[right][1]]
            elif s < target:
                left += 1
            else:
                right -= 1

        return []


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3, 3], 6))
    print(s.twoSum([3, 2, 4], 6))
    print(s.twoSum([2, 7, 11, 15], 9))
