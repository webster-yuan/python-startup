# 在一个火车旅行很受欢迎的国度，你提前一年计划了一些火车旅行。在接下来的一年里，
# 你要旅行的日子将以一个名为 days 的数组给出。每一项是一个从 1 到 365 的整数。

# 火车票有 三种不同的销售方式 ：

# 一张 为期一天 的通行证售价为 costs[0] 美元；
# 一张 为期七天 的通行证售价为 costs[1] 美元；
# 一张 为期三十天 的通行证售价为 costs[2] 美元。
# 通行证允许数天无限制的旅行。 例如，如果我们在第 2 天获得一张 为期 7 天 的通行证，
# 那么我们可以连着旅行 7 天：第 2 天、第 3 天、第 4 天、第 5 天、第 6 天、第 7 天和第 8 天。

# 返回 你想要完成在给定的列表 days 中列出的每一天的旅行所需要的最低消费 。


# 1. dfs
#   状态定义：
# 我希望有一个函数,可以告诉我从days[i....] （第i下标位置天开始到最后）,我能完成旅行的最低消费
#   状态转移方程：
# 有三种选择,选择最小消费并且可以完成旅行
# dfs(i) = min(
#     costs[0] + dfs(next_index_1),
#     costs[1] + dfs(next_index_7),
#     costs[2] + dfs(next_index_30)
# )
#
# 需要辅助逻辑，这个涉及到枚举三种选择以及后续造成的影响
# 所以可变的参数只有一个，就是next_index的值，
#   next_index 表示：当前通行证失效后，第一个还未被覆盖的旅行日
# 那这个可以用循环去寻找，因为 days 中的元素代表日期，肯定是递增的，所以可以用 while 找到第一个不被覆盖的位置
# days = [1,4,6,7,8,20], costs = [2,7,15]
#   边界条件: 所有天数都完成旅行,cur_index>=n
#   说明：
# 只在旅行日做决策是最优的，因为非旅行日不需要购票

from typing import List


def mincostTickets_memo_dfs(self, days: List[int], costs: List[int]) -> int:
    m = len(days)
    n = len(costs)
    memo = {}
    durations = [1, 7, 30]

    def dfs(cur_index: int):
        if cur_index >= m:
            return 0

        if cur_index in memo:
            return memo[cur_index]

        min_cost = float("inf")

        # 三种选择方式，然后再分别去寻找能到达的最远的位置
        for i in range(n):
            next_index = cur_index
            duration = durations[i]
            while next_index < m and days[cur_index] + duration > days[next_index]:
                next_index += 1

            # 循环退出，找到了这次选择没能覆盖的位置，也就是应该做下一个决策的位置
            min_cost = min(min_cost, dfs(next_index) + costs[i])

        memo[cur_index] = min_cost
        return min_cost

    return dfs(0)


# dp:
# 状态定义： dp[i]代表的就是从第days[i]天开始，并且满足旅行到最后的，最小花费
# 状态转移：dp[i] = min(
#           costs[0] + dp[next_index_1],
#           costs[1] + dp[next_index_2],
#           costs[2] + dp[next_index_3],
# )
# 初始化：左依赖于右，dp[i] 依赖未来状态 dp[next_index]
# 从右往左找，因为最后一个元素也涉及到计算，所以多开一个空间在右边，作为越界之后的终止条件
# dp[m] = 0
def mincostTickets_dp(self, days: List[int], costs: List[int]) -> int:
    m = len(days)
    n = len(costs)
    dp = [0 for _ in range(m + 1)]
    durations = [1, 7, 30]
    # T: O(N^2)
    for i in range(m - 1, -1, -1):
        min_cost = float("inf")
        for j in range(n):
            next_index = i
            duration = durations[j]
            while next_index < m and days[i] + duration > days[next_index]:
                next_index += 1

            # 循环退出，找到了这次选择没能覆盖的位置，也就是应该做下一个决策的位置
            min_cost = min(min_cost, dp[next_index] + costs[j])

        dp[i] = min_cost

    return dp[0]


# bisect.bisect_left 是 Python 内置模块 bisect 中的核心函数，专门用于在有序列表中查找指定元素的插入位置，
# 且能保证插入后列表仍保持升序，是处理有序序列的高效工具（时间复杂度为 O(logn)）。
import bisect


def mincostTickets_plus(self, days: List[int], costs: List[int]) -> int:
    m = len(days)
    n = len(costs)
    dp = [0 for _ in range(m + 1)]
    durations = [1, 7, 30]
    # T: O(NlogN)
    for i in range(m - 1, -1, -1):
        min_cost = float("inf")
        for j in range(n):
            next_index = i
            duration = durations[j]
            next_index = bisect.bisect_left(days, days[i] + duration)
            min_cost = min(min_cost, dp[next_index] + costs[j])

        dp[i] = min_cost

    return dp[0]


# 对于每个 i，找：
# 第一个 ≥ days[i] + 1 的位置 p1
# 第一个 ≥ days[i] + 7 的位置 p2
# 第一个 ≥ days[i] + 30 的位置 p3
# 现在是 从右往左遍历 i
# 指针是“从左往右移动的”
# 所以需要修改：必须改成从左往右 DP，
# 状态定义：dp[i] = 前 i 天（days[0..i-1]）的最小花费
# 初始化：为了将m边界值也纳入计算，所以多开一个空间，作为终止条件，dp[m]=0
# 状态转移：
# dp[i + 1] = min(
#             costs[0] + dp[p1],
#             costs[1] + dp[p2],
#             costs[2] + dp[p3],
#         )
# T = O(n)
def mincostTickets_best(self, days: List[int], costs: List[int]) -> int:
    m = len(days)
    n = len(costs)
    dp = [0 for _ in range(m + 1)]
    p1 = p2 = p3 = 0
    # T: O(N)
    for i in range(m):
        while days[p1] < days[i] - 0:
            p1 += 1
        while days[p2] < days[i] - 6:
            p2 += 1
        while days[p3] < days[i] - 29:
            p3 += 1

        dp[i + 1] = min(
            costs[0] + dp[p1],
            costs[1] + dp[p2],
            costs[2] + dp[p3],
        )

    return dp[m]
