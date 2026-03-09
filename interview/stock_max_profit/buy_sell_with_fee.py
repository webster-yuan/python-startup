# 每次卖出需要支付手续费，可多次交易，求最大利润
# 2 个状态：持有 / 未持有，卖出时扣除手续费
# 每天都可以选择是继续买入,还是直接卖
# 最后一天肯定是卖出才是最高利润,所以直接返回cash

def max_profit(nums:list[int], fee:int):
    if len(nums)<2:
        return 0
    
    hold = -nums[0] # 假设第一天买入,利润为负
    cash = 0 # 初始状态未持有，利润为0

    for num in nums[1:]:
        # 状态转移:卖出时扣除手续费
        hold = max(hold, cash - num) # 今天可以不动,或者再一次买入
        cash = max(cash, hold+num-fee) # 今天可以不动,或者卖出（扣除手续费）

    return cash

print(max_profit([1,3,2,8,4,9], 2))  # (8-1-2)+(9-4-2) = 8