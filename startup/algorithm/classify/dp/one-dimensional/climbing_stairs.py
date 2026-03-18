# 题目：有 n 阶楼梯，每次能爬 1 或 2 阶，求有多少种不同的方法爬到楼顶。
# 状态定义：dp[i] = 爬到第 i 阶的方法数；
# 转移方程：dp[i] = dp[i-1] + dp[i-2]（最后一步要么爬 1 阶，要么爬 2 阶）；
# 初始条件：dp[1]=1，dp[2]=2。


def dfs(n: int):
    if n <= 2:
        return n

    return dfs(n - 1) + dfs(n - 2)


print(dfs(3))  # 3种（1+1+1 / 1+2 / 2+1）
print(dfs(5))  # 8种（可以手动数验证）

memo = {}


def memo_dfs(n: int):
    if n <= 2:
        return n

    if n in memo:
        return memo[n]

    res = memo_dfs(n - 1) + memo_dfs(n - 2)
    memo[n] = res
    return res


print(memo_dfs(3))  # 3种（1+1+1 / 1+2 / 2+1）
print(memo_dfs(5))  # 8种（可以手动数验证）


def climbStairs(n: int):
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print(climbStairs(3))  # 3种（1+1+1 / 1+2 / 2+1）
print(climbStairs(5))  # 8种（可以手动数验证）


def climbStairs_optimized(n: int):
    if n <= 2:
        return n

    prev_prev = 1
    prev = 2
    # 从3开始，循环计算当前值
    for _ in range(3, n + 1):
        cur = prev_prev + prev
        # 变量转移
        prev_prev = prev
        prev = cur

    return prev


print(climbStairs_optimized(3))
print(climbStairs_optimized(5))
