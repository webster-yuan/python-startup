# 01 背包问题（文远智行面试高频进阶 DP）
# 题目复述（简化版，面试常考）
# 有 n 个物品，每个物品有重量 weight[i] 和价值 value[i]，还有一个容量为 C 的背包。
# 每个物品只能选一次（0 = 不选，1 = 选），问背包能装的最大价值是多少？

# 1.dfs : 有一个函数能告诉我在从第i件商品开始选时,并且还剩下容量c时,能获得的最大价值
# 边界: weight[i] > c 不能选了, 或者n个物品选完了
# 递归关系: 1选了,dfs(i,c) = dfs(i+1,c-weight[i]) + value[i]
#          0没选,dfs(i,c) = dfs(i+1, c) +value[i]
# dfs(i,j) = max(dfs(i+1,c-weight[i]) + value[i] , dfs(i+1, c) +value[i])


def dfs(i, c, weight: list[int], n, value: list[int]):
    if i >= n:
        return 0

    if c < weight:
        return dfs(i + 1, c, weight, n, value)

    # 两种选择
    return max(
        dfs(i + 1, c - weight[i], weight, n, value) + value[i],
        dfs(i + 1, c, weight, n, value),
    )


# 2. memo
def knapsack_01_memo_dfs(weight: list[int], value: list[int], C):
    n = len(weight)
    memo = [[-1] * (C + 1) for _ in range(n)]

    def memo_dfs(i, c):
        if i >= n:
            return 0

        if memo[i][c] != -1:
            return memo[i][c]

        res = 0
        if c < weight[i]:
            res = memo_dfs(i + 1, c)
        else:
            res = max(memo_dfs(i + 1, c - weight[i]) + value[i], memo_dfs(i + 1, c))

        memo[i][c] = res
        return res

    return memo_dfs(0, C)


print(knapsack_01_memo_dfs([2, 3, 4, 5], [3, 4, 5, 6], 8))  # 输出10，正确

# dp
# 从如上memo分析得知，(i,c) 上依赖于下，当前行 i 的状态，只依赖下一行 i+1 的状态， 所以是从底往上推
# c 对于容量维度 c：在基础版二维 DP 中，c 依赖的值都在i+1行，
# 而 i+1 行的 c 和 c - weight [i] 都已经在之前算过了，不存在 “依赖左边还是右边” 的问题

# dp[i][c] 就代表从i开始选择，容量还剩下c时，能得到的最大价值
# dp[i][c] = max(dp[i+1][c], dp[i+1][c-weight[i]]+value[i])
# 边界：最后一行，也就是处理最后一个物品的时候，如果空间够，肯定选上，不够就不选了
# dp[n-1][c] = value[n-1] if c >weight[n-1] else 0


def knapsack_01_dp(weight: list[int], value: list[int], C):
    n = len(weight)
    dp = [[-1] * (C + 1) for _ in range(n)]

    # 先处理最后一个物品（i = n-1）处理最后一行的每一列
    for c in range(C + 1):
        if c >= weight[n - 1]:
            dp[n - 1][c] = value[n - 1]
        else:
            dp[n - 1][c] = 0  # 对应i == n的边界值

    for i in range(n - 2, -1, -1):
        for c in range(C + 1):
            res = 0
            if c < weight[i]:
                res = dp[i + 1][c]
            else:
                res = max(dp[i + 1][c - weight[i]] + value[i], dp[i + 1][c])

            dp[i][c] = res

    return dp[0][C]


print(knapsack_01_dp([2, 3, 4, 5], [3, 4, 5, 6], 8))
