# 题目复述
# 一个 m x n 的网格，
# 机器人从左上角出发，每次只能向右或向下移动一步，
# 问有多少种不同的路径到达右下角？


# 1. dfs:
# 状态：dfs(i,j) 返回 “从 (i,j) 到终点的路径数”
# 边界：当i==m-1或j==n-1时，返回 1
# 初始化：dfs(m-1,n-1)=1
def dfs(i, j, m, n):
    if i == m - 1 and j == n - 1:
        return 1

    # if-return 是隐形互斥
    if i == m - 1:
        return dfs(i, j + 1, m, n)

    if j == n - 1:
        return dfs(i + 1, j, m, n)

    return dfs(i, j + 1, m, n) + dfs(i + 1, j, m, n)


def unique_paths_memo_dfs(m, n):
    memo = [[-1] * n for _ in range(m)]

    def memo_dfs(i, j):
        if i == m - 1 and j == n - 1:
            return 1

        if memo[i][j] != -1:
            return memo[i][j]

        res = 0
        # if-elif-else 直观互斥
        if i == m - 1:
            res = memo_dfs(i, j + 1)
        elif j == n - 1:
            res = memo_dfs(i + 1, j)
        else:
            res = memo_dfs(i + 1, j) + memo_dfs(i, j + 1)

        memo[i][j] = res
        return res

    return memo_dfs(0, 0)


print(unique_paths_memo_dfs(3, 7))

# 从dfs推到过来发现：左上依赖于右下
# 所以是从右往左，从下往上进行递推的
# dp[i][j]就代表从(i,j)位置到达(m-1,n-1)位置的路径数
# dp[m-1][n-1] = 1
# dp[i][j] = dp[i+1][j] + dp[i][j+1]


def unique_paths_dp(m, n):
    # 覆盖最后一行,最后一列数值都为1的情况
    dp = [[1] * n for _ in range(m)]
    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

    return dp[0][0]


print(unique_paths_dp(3, 7))
