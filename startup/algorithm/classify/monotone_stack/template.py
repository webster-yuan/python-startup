from collections import deque
from typing import List


# https://www.nowcoder.com/practice/2a2c00e7a88a498693568cef63a4b7bb
# 对python语言不友好，尝试各种办法仍然超时，但逻辑本身没有问题

class Solution:
    def monotone_stack(self, nums: List[int]) -> List[List[int]]:
        """
        给定一个数组（假设没有重复元素），对应返回左右最近的，比index位置元素小的元素下标
        0: 存左边比index位置小的元素index
        1: 存右边比index位置小的元素index
        """
        monotone_stack = deque()  # 它提供了 O(1) 时间的 append()（入栈）和 pop()（出栈）操作
        result = [[-1, -1] for _ in range(len(nums))]
        for index, num in enumerate(nums):
            while len(monotone_stack) != 0 and num < nums[monotone_stack[-1]]:  # monotone_stack[-1]查看栈顶（不弹出），注意我们存放的是下标
                # 当栈不为空，或者当前值比栈顶元素大时，走以下逻辑，维护 从栈底到栈顶的从小到大的逻辑
                # 应该弹出栈顶元素，并对栈顶元素的左右较小值进行统计
                # 左边比自己小的，那就是自己压着的元素
                # 右边比自己小的，就是让自己弹出时的元素
                cur_top_num_index = monotone_stack.pop()
                if len(monotone_stack) != 0:
                    result[cur_top_num_index][0] = monotone_stack[-1]
                else:
                    result[cur_top_num_index][0] = -1

                result[cur_top_num_index][1] = index

            # 将当前元素入栈
            monotone_stack.append(index)

        # 遍历原数组完成之后，处理栈中剩下的元素
        while len(monotone_stack) > 0:
            cur_top_num_index = monotone_stack.pop()
            if len(monotone_stack) != 0:
                result[cur_top_num_index][0] = monotone_stack[-1]
            else:
                result[cur_top_num_index][0] = -1

            result[cur_top_num_index][1] = -1  # 右边没有比自己更小的

        # print(result)
        return result


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split(' ')))
    # print(nums)
    s = Solution()
    result = s.monotone_stack(nums)
    for l, r in result:
        print(f"{l},{r}")
