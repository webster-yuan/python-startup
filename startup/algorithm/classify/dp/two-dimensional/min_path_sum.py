# 题目复述
# 一个 m x n 的网格，每个格子有一个非负整数 grid[i][j]，
# 机器人从左上角出发，每次只能向右或向下移动，
# 求到达右下角的最小路径和
# （路径和 = 路径上所有格子的数字之和）。

# 1. dfs: 我希望有个函数告诉我,从(i,j)位置到达右下角的最小路径和
# 状态: dfs(i,j)
# 边界: 到达m-1只能往右走,到达n-1只能往下走,并且加上此处数值
# 初始化: dfs(m-1)(n-1) = grid[m-1][n-1]


def dfs(i, j, m, n, grid):
    if i == m - 1 and j == n - 1:
        return grid[i][j]

    if i == m - 1:
        return grid[i][j] + dfs(i, j + 1, m, n, grid)
    if j == n - 1:
        return grid[i][j] + dfs(i + 1, j, m, n, grid)

    return grid[i][j] + min(dfs(i, j + 1, m, n, grid), dfs(i + 1, j, m, n, grid))


# 2. memo
def min_path_sum_memo_dfs(grid):
    m = len(grid)
    n = len(grid[0])
    memo = [[-1] * n for _ in range(m)]

    def memo_dfs(i, j):
        if i == m - 1 and j == n - 1:
            return grid[i][j]

        if memo[i][j] != -1:
            return memo[i][j]

        res = 0
        if i == m - 1:
            res = grid[i][j] + memo_dfs(i, j + 1)
        elif j == n - 1:
            res = grid[i][j] + memo_dfs(i + 1, j)
        else:
            res = grid[i][j] + min(memo_dfs(i, j + 1), memo_dfs(i + 1, j))

        memo[i][j] = res
        return res

    return memo_dfs(0, 0)


print(min_path_sum_memo_dfs([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))

# 3. dp
# 从memo发现,状态是左依赖右,上依赖下,
# 所以推导关系是右推导左,下推导上
# 状态定义: dp[i][j]代表的就是dfs的含义: 从 (i,j) 到终点的最小路径和
# 转移关系: dp[i][j] = grid[i][j]+min(dp[i+1,j],dp[i][j+1])
# 初识条件: dp[m-1][n-1] = grid[i][j]
#          最后一行: dp[m-1][j] = grid[m-1][j] + dp[m-1][j+1]
#          最后一列: dp[i][n-1] = grid[i][n-1] +dp[i+1][n-1]


def min_path_sum_dp(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0] * n for _ in range(m)]

    dp[m - 1][n - 1] = grid[m - 1][n - 1]
    # 最后一行,从右往左填充每一列
    for j in range(n - 2, -1, -1):
        dp[m - 1][j] = grid[m - 1][j] + dp[m - 1][j + 1]

    # 最后一列,从下往上填充每一行
    for i in range(m - 2, -1, -1):
        dp[i][n - 1] = grid[i][n - 1] + dp[i + 1][n - 1]

    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])

    return dp[0][0]


print(min_path_sum_dp([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
