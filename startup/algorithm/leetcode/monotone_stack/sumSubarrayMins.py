from collections import deque
from typing import List


class Solution:
    """
    https://leetcode.cn/problems/sum-of-subarray-minimums/description/
    """

    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        求cur_index位置的向左最小值left_index，向右较小值right_index，
        那么在[left_index+1, right_index-1]这个区间内的，包含cur_index的数组组合中，
        最小值一定是cur_index位置对应的值，这样的组合的个数 count=?
        一个子数组 = 左端点的选择 × 右端点的选择

        左端点在[left_index+1, cur_index]区间里面，有 cur_index - (left_index + 1) + 1 种
        左端点在[cur_index, right_index-1]区间里面，有 right_index - 1 - cur_index + 1 种
        每一个左端点，都可以搭配 任意一个右端点
        左右端点都选 cur_index，代表的正是「长度为 1 的子数组 [cur_index, cur_index]」。
        它只会被算一次，而且必须被算一次
        即 count = (cur_index - left_index) * (right_index - cur_index)

        针对重复数字的情况分析，不用考虑，详见：https://www.bilibili.com/video/BV1HH4y1X7T9?t=4183.4
        todo:
        1. 维护一个单调栈，大压小实现求左右距离最近的比自己小的元素的位置
        2. 根据公式 count 计算每个点作为最小值出现在多个组合中的累加和，sum(cur_index) = count(cur_index) * arr[cur_index]
        """
        monotone_stack = deque()
        mod = 10 ** 9 + 7
        total_count = 0
        for index, num in enumerate(arr):
            while len(monotone_stack) > 0 and arr[monotone_stack[-1]] > num:
                cur_top_num_index = monotone_stack.pop()
                left_index = monotone_stack[-1] if len(monotone_stack) > 0 else -1
                right_index = index
                cur_num_count = (cur_top_num_index - left_index) * (
                        right_index - cur_top_num_index)

                total_count = (total_count + arr[cur_top_num_index] * cur_num_count) % mod

            monotone_stack.append(index)

        while len(monotone_stack) > 0:
            cur_top_num_index = monotone_stack.pop()
            left_index = monotone_stack[-1] if len(monotone_stack) > 0 else -1
            right_index = len(arr)
            cur_num_count = (cur_top_num_index - left_index) * (
                    right_index - cur_top_num_index)
            total_count = (total_count + arr[cur_top_num_index] * cur_num_count) % mod

        return total_count


if __name__ == '__main__':
    s = Solution()
    print(s.sumSubarrayMins([3, 1, 2, 4]))
