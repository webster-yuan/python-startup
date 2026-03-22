from typing import List

# 只记录「长度」，无法正确统计「个数」，
# 因为「相同长度的子序列，可能来自不同的路径，且路径数无法通过长度直接推导」。
# 用一个具体例子帮你说清楚为什么只记录长度会出错：
# 反例：nums = [1,3,5,4,7]
# 我们先看「以 1 为起点」的情况：
# 路径 1：1 → 3 → 5 → 7（长度 4）
# 路径 2：1 → 3 → 4 → 7（长度 4）
# 如果只记录 dp_len[0] = 4，
# 只能知道「以 1 为起点的最长长度是 4」，
# 但无法知道这个长度对应 2 种路径—— 而这正是题目要求的「个数」。

# 在求解最大长度的同时去维护一个栈（举例）然后记录最大长度的个数，
# 本质上也是定义了两种状态


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        1. 状态定义
        dfs_len[i]：以 nums[i] 为起点的最长递增子序列长度（和之前 LIS 问题一致）；
        dfs_cnt[i]：以 nums[i] 为起点的最长递增子序列的个数（新增的计数状态）。
        2. 递归逻辑
        对于 i，遍历后面所有 j (j > i)，如果 nums[j] > nums[i]：
            若 dfs_len[j] + 1 > dfs_len[i]：说明找到了更长的子序列，
                更新 dfs_len[i] = dfs_len[j] + 1，
                同时 dfs_cnt[i] = dfs_cnt[j]（新的计数等于 j 的计数）；
            若 dfs_len[j] + 1 == dfs_len[i]：说明找到了相同长度的子序列，
                累加计数 dfs_cnt[i] += dfs_cnt[j]；
            边界：如果 i 是最后一个元素，dfs_len[i] = 1，dfs_cnt[i] = 1（只有自己，长度 1，计数 1）。
        3. 最终结果
        先找到全局最长递增子序列的长度 max_len；
        遍历所有 i，累加所有 dfs_len[i] == max_len 的 dfs_cnt[i]，就是答案。
        """
        n = len(nums)
        memo_len = [-1] * n
        memo_cnt = [-1] * n

        def memo_dfs(i):
            if memo_len[i] != -1:
                return memo_len[i], memo_cnt[i]

            max_len = 1
            max_cnt = 1

            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    sub_len, sub_cnt = memo_dfs(j)
                    current_len = sub_len + 1

                    # 更新cnt值
                    # case1 找到了更长的子系列
                    if current_len > max_len:
                        max_len = current_len
                        max_cnt = sub_cnt
                    elif current_len == max_len:
                        max_cnt += sub_cnt

            memo_len[i] = max_len
            memo_cnt[i] = max_cnt
            return max_len, max_cnt

        all_len = []
        all_cnt = []
        for i in range(n):
            l, c = memo_dfs(i)
            all_len.append(l)
            all_cnt.append(c)

        max_total_len = max(all_len)

        result = 0
        for i in range(n):
            if all_len[i] == max_total_len:
                result += all_cnt[i]

        return result

    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        状态定义:
        dp_len[i]代表以i为起点,[i...]区间中最长子序列的长度
        dp_cnt[i]代表以i为起点,[i...]区间中最长子系列的长度的个数

        状态转移:
        if nums[j] > nums[i],
            current_len = dp_len[j]+1

            if current_len > dp_len[i]:
                dp_len[i] = current_len
                dp_cnt[i] = dp_cnt[j]
            elif current_len == dp_len[i]:
                dp_cnt[i] += dp[j]

        初始化:
            dp_len[i]=1 dp_cnt[i]=1

        返回值：
            找全局最大长度，累加求和
        """
        n = len(nums)
        dp_len = [1] * n
        dp_cnt = [1] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    current_len = dp_len[j] + 1
                    if current_len > dp_len[i]:
                        dp_len[i] = current_len
                        dp_cnt[i] = dp_cnt[j]
                    elif current_len == dp_len[i]:
                        dp_cnt[i] += dp_cnt[j]

        max_len = max(dp_len)
        res = 0
        for i in range(n):
            if dp_len[i] == max_len:
                res += dp_cnt[i]

        return res
