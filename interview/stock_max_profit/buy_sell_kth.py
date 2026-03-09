# 最多交易k次
# dfs(day, remain_key, hold)：表示「第 day 天，还能交易 remain_key 次，当前是否持有股票」时的最大利润。
# hold是 0/1：0 = 未持有，1 = 持有。

# 每天的选择
# 不操作：利润不变，直接走到下一天 → dfs(day+1, remain_k, hold)
# 买入：仅当hold=0且remain_k>0时可行，利润减少当前股价，remain_k-1，持有状态变为 1 → dfs(day+1, remain_k-1, 1) - prices[day]
# 卖出：仅当hold=1时可行，利润增加当前股价，持有状态变为 0 → dfs(day+1, remain_k, 0) + prices[day]

# 终止条件
# day == len(prices)：没有更多的天数可供选择，利润为 0

# 记忆化剪枝

def max_profit(nums:list[int], k:int):
    n = len(nums)
    if n < 2:
        return 0
    
    # memo[day][remain_k][hold] [n+1][k+1][2]
    memo = [[[-1] * 2 for i in range(k+1)] for _ in range(n)]

    def dfs(day, remain_k ,hold):
        if day == n:
            return 0
        
        # 查缓存,有值直接返回
        if memo[day][remain_k][hold] != -1:
            return memo[day][remain_k][hold]
        
        # 选择一: 不操作
        no_action = dfs(day+1, remain_k, hold)

        # 选择二: 买入
        buy = float('-inf')
        if hold ==0 and remain_k >0:
            buy= dfs(day+1, remain_k-1, 1) - nums[day]
        
        # 选择三: 卖出
        sell = float('-inf')
        if hold == 1:
            sell = dfs(day+1, remain_k, 0) + nums[day]
        
        # 当前状态最大利润 = 三种选择的最大值
        res = max(no_action, buy, sell)
        memo[day][remain_k][hold] =res
        return res
    
    return dfs(0, k , 0)

print(max_profit([3,2,6,5,0,3],2))  # (6-2)+(3-0) = 7



