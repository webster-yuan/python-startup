# 题干

# 给定一个整数数组 nums，你最初位于数组的 第一个下标。

# 数组中的每个元素 nums[i] 表示你在该位置 最多可以跳跃的步数。

# 判断你是否能够到达 最后一个下标。

# 示例
# 输入: nums = [2,3,1,1,4]
# 输出: True
# 解释: 0 → 1 → 4
# 输入: nums = [3,2,1,0,4]
# 输出: False
# 解释: 到达 index=3 后无法继续跳跃
# 最优解（贪心 O(n)）

# 核心思想：

# 维护当前能到达的 最远位置 max_reach

def can_jump(nums: list[int]) -> bool:

    max_reach = 0

    for i in range(len(nums)):
        if i > max_reach:
            """
            我们之前积累的能到的最远的位置，是不能够 到达这个i位置的，后续肯定也到不了
            """
            return False

        max_reach = max(max_reach, i + nums[i])

    return True


print(can_jump([2,3,1,1,4]))  # True
print(can_jump([3,2,1,0,4]))  # False
print(can_jump([0]))          # True
print(can_jump([1,0,1]))      # False
