# 最多买卖两次（不能同时持有），求最大利润
# 定义 4 个状态：
# buy1：第一次买入后的最大利润
# sell1：第一次卖出后的最大利润
# buy2：第二次买入后的最大利润
# sell2：第二次卖出后的最大利润

# 因为第二次交易的利润结果来源于第一次交易的结果
# 假设最高利润是只交易一次，那么第二次交易肯定比第一次的利润低

def max_profit(nums:list[int]):
    if len(nums)<2:
        return 0
    
    # 初始化四种状态，假设第一天买入了
    buy1 = -nums[0]
    sell1 = 0
    buy2 = -nums[0]
    sell2 = 0

    for num in range(1, len(nums)):
        new_buy1 = max(buy1, -nums[num])
        new_sell1 = max(sell1, buy1+nums[num])
        new_buy2 = max(buy2, sell1-nums[num])
        new_sell2 = max(sell2, buy2+nums[num])

        buy1, sell1, buy2, sell2 = new_buy1, new_sell1, new_buy2, new_sell2

    return sell2

# 测试用例
print(max_profit([3,3,5,0,0,3,1,4]))  # (3-0)+(4-1) = 6
print(max_profit([1,2,3,4,5]))        # 5-1 = 4（只交易一次更优）