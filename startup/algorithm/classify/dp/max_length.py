from typing import List

# https://leetcode.cn/problems/longest-increasing-subsequence/description/


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        dfs(i)代表从[i...]中，最长递增子系列的长度是多少
        遍历每一个元素，分别作为起点i，执行dfs，然后对比长度最大值得到子系列最大长度
        然后从i位置开始向后遍历，统计已i为起点得到子系列的最大长度
        边界条件：if i==n，return 0

        即使[i...]的最长子系列不一定是以i开始的，但是因为我们在外层遍历了每一个元素作为开头的所有情况，
        所以一定不会存在遗漏的情况
        「强制以 i 开头」的设计，是为了让递归逻辑更清晰，避免重复枚举（比如同一个子序列不会被多个 dfs(i) 重复统计）。
        """
        n = len(nums)
        memo = [-1] * n

        def memo_dfs(i):
            if memo[i] != -1:
                return memo[i]

            meta_max_length = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    current = memo_dfs(j) + 1
                    if current > meta_max_length:
                        meta_max_length = current

            memo[i] = meta_max_length
            return meta_max_length

        max_length = 0
        for i in range(n):
            max_length = max(max_length, memo_dfs(i))

        return max_length

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        dp：
        状态定义：dp[i]代表以[i...]位置开始最长子系列的长度
        初始化：dp[i]=1
        依赖关系：左依赖于右，所以是从右往左推
        """
        n = len(nums)
        if n == 0:
            return 0

        dp = [1] * n
        # 从右往左计算
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
