# 题干

# 给定一个整数数组 nums，你最初位于数组的 第一个下标。

# 数组中的每个元素 nums[i] 表示你在该位置 最多可以跳跃的步数。

# 保证一定可以到达最后一个位置。

# 返回 到达最后一个位置的最少跳跃次数。

# 示例
# 输入: nums = [2,3,1,1,4]
# 输出: 2

# 解释:
# 0 → 1 → 4
# 最优解（贪心 O(n)）

# 思想：

# max_reach 当前能到达的最远位置

# end 当前这一跳的边界

# steps 跳跃次数

def min_jump(nums: list[int]) -> int:
    n = len(nums)

    max_reach = 0
    end = 0
    steps = 0

    for i in range(n - 1):
        max_reach = max(max_reach, i + nums[i])

        if i == end:
            """
            当前这最远的一跳已经结束，需要记录步数，更新下一跳的最远位置为新的结束判定点
            """
            steps += 1
            end = max_reach

    return steps

print(min_jump([2,3,1,1,4]))  # 2
print(min_jump([2,3,0,1,4]))  # 2
print(min_jump([1,1,1,1]))    # 3
print(min_jump([4,1,1,3,1,1,1]))  # 2