# 卖出后第 2 天才能买入（冷冻期 1 天），可以多次交易，求最大利润
# hold：持有股票的最大利润
# freeze：冷冻期的最大利润（刚卖出）
# free：非冷冻期且未持有股票的最大利润


def max_profit(nums):
    if len(nums)<2:
        return 0
    
    hold = -nums[0] # 假设第一天买入,利润为负
    freeze = 0 # 刚卖出,冷冻期的最大利润
    free = 0 # 非冷冻期且未持有股票的最大利润

    for num in nums[1:]:
        new_hold = max(hold, free - num) # 今天不动,或者继续买入
        new_freeze = hold + num # 因为今天是冷冻期,所以只能卖出一种选择
        new_free = max(free, freeze) # 两种状态来源: 1. 今天不动,保持非冷冻期未持有状态; 2. 刚卖出,进入冷冻期,所以取两者的最大值
        hold , freeze, free = new_hold, new_freeze, new_free
    
    return max(freeze, free) # 最后一天肯定是卖出才是最高利润,所以直接返回freeze和free的最大值

print(max_profit([1,2,3,0,2]))  # (2-1)+(2-0) = 3（卖出2后冷冻期，第4天买0）