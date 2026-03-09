# 可以多次买卖（但不能同时持有多只），求最大利润

# 贪心算法 —— 只要后一天价格比前一天高，就买入卖出（累加所有正差价）

def max_profit(nums:list[int]):
    if len(nums) < 2:
        return 0
    
    profit = 0
    for i in range(1, len(nums)):
        # 只要当天比前一天价格高，就买入卖出
        if nums[i] > nums[i-1]:
            profit += nums[i] - nums[i-1]
    
    return profit

# 测试用例
print(max_profit([7,1,5,3,6,4]))  # (5-1)+(6-3) = 7
print(max_profit([1,2,3,4,5]))    # (2-1)+(3-2)+(4-3)+(5-4) = 4