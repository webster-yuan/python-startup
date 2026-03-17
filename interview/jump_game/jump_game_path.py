# 题干
# 给定一个整数数组 nums，你最初位于数组的 第一个下标。
# 数组中的每个元素 nums[i] 表示你在该位置 最多可以跳跃的步数。
# 如果能够到达最后一个下标：
# 返回 最少跳跃次数的一条路径（下标表示）。
# 如果无法到达：
# 返回 (False, [])

# 示例
# 输入
# nums = [2,3,1,1,4]

# 输出
# (True, [0,1,4])

def get_path(nums: list[int]):
    n = len(nums)

    if n == 0:
        return False, []

    max_reach = 0
    end = 0
    best_pos = 0

    path = [0]

    for i in range(n):

        if i > max_reach:
            """
            当前位置，在之前的数组维护的最远位置到达不了，那么说明后续[i:]以后的位置都到达不了
            """
            return False, []

        if i + nums[i] > max_reach:
            """
            更新从当前位置能到达的最远距离的同时，记录此时的位置
            因为从i位置能跳的更远，所以我们选择这个点
            """
            max_reach = i + nums[i]
            best_pos = i

        if i == end:
            """
            这一最优跳已经结束
            """
            if i != 0:
                path.append(best_pos)
            
            # 更新下一最优跳结束的标识
            end = max_reach
            
            # 如果已经跳过了最后一个位置，也是可以跳到的证明
            if end >= n - 1:
                path.append(n - 1)
                return True, path

    return False, []

nums1 = [2,3,1,1,4]
nums2 = [1,0,3]
nums3 = [2,1,1,1,4]

print(get_path(nums1))
# (True, [0, 1, 4])

print(get_path(nums2))
# (False, [])

print(get_path(nums3))
# (True, [0, 2, 4])