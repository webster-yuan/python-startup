from typing import List


def change_memo_dfs(amount: int, coins: List[int]) -> int:
    """
    状态定义：
        希望有个函数告诉我凑齐remain_count这些钱，在[i:]的区间中，有多少种组合的方式
    边界值：
        remain_count = 0 时，代表能够凑出，这个可以作为一个组合方式，所以返回1
        remain_count<0，代表超过了，凑不出来，返回0
        index ==m: 说明硬币里面的情况都遍历完了还没凑出来，返回0

    状态转移：当前硬币可以选，可以不选
        选了可以重复选这个，res += dfs(remain_count-coins[index], index)
        没选：res += dfs(remain_count, index+1)
    记忆化搜索：
        可变参数有两个，硬币选择下标和剩下的目标值，memo[(index, remain_count)] = x
    """
    m = len(coins)
    memo = {}

    def dfs(remain_count: int, index):
        if remain_count == 0:
            return 1

        if remain_count < 0:
            return 0

        if index == m:
            return 0

        if (index, remain_count) in memo:
            return memo[(index, remain_count)]

        path_count = dfs(remain_count, index + 1) + dfs(
            remain_count - coins[index], index
        )  # 选当前硬币，可以重复选，所以不用下标移动
        memo[(index, remain_count)] = path_count
        return path_count

    return dfs(amount, 0)


def change_memo_dp(amount: int, coins: List[int]) -> int:
    """
    dp:
        状态定义：dp[i][remain] 代表 从第 i 个硬币开始选择（可以重复选），凑出金额 remain 的组合数
        状态转移：dp[i][remain] = dp[i+1][remain] + dp[i][remain-coins[i]]
        前提：当 remain >= coins[i] 才能选
        初始化：
        remain=0 代表第一列，初始化为1；→ 凑出 0 元，不用选就是一种方案
        dp[m][0] = 1 所以要多开一行，m+1行，记录这个状态
        index=m remain > 0 代表还没凑出来，多开一行在下面，初始化为0

        依赖关系：
            右依赖于左，所以是从左往右推，上依赖于下，所以是从下上推
            
    """
    m = len(coins)
    dp = [[0]*(amount+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = 1
    
    for i in range(m-1, -1, -1):
        for j in range(amount+1):
            if j < coins[i]:
                dp[i][j] = dp[i+1][j]
            else:
                dp[i][j] = dp[i+1][j] + dp[i][j-coins[i]]
        
    return dp[0][amount]

def change_memo_plus(amount: int, coins: List[int]) -> int:
    """
    plus:
        根据依赖关系，发现dp[i][j]依赖于dp[i+1][j]或者dp[i][j-x]
        如果是从下往上遍历，dp[i+1][j]就是原始dp[i][j]位置的值
        进一步保障从左往右遍历的话，dp[i][j-x]的值一定是已经算过的
        所以可以优化为一维的数组 amount+1列
        i 就是为了获取硬币，直接先遍历硬币即可，顺序可以不管，只要保证不重复就行
    状态调整：dp[j] 表示：当前已经处理过的硬币，凑出 j 的组合数

    """
    dp= [0] * (amount+1)
    dp[0] = 1
    for coin in coins:
        for j in range(coin, amount+1):
            dp[j] = dp[j] + dp[j-coin]
        
    return dp[amount]

