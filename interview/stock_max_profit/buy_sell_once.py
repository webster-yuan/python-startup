# 股票选择
# 给定一个数组，代表股票每天的价格，
# 可以在任何一天买入，任何一天卖出，求最大利润
# 只能买卖一次
# 求最大利润

def max_profit(nums):
    if not nums:
        return 0
    
    min_val = nums[0]
    res = 0
    for num in nums:
        min_val = min(min_val, num)
        res = max(res, num-min_val)

    return res


def test_cases():
    # 批量测试用例
    test_cases = [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
        ([1,2,3,4,5], 4),
        ([5], 0),
        ([], 0),
        ([2,4,1,7,3,9], 8)
    ]

    # 执行测试
    for i, (nums, expected) in enumerate(test_cases):
        actual = max_profit(nums)
        status = "✅ 正确" if actual == expected else "❌ 错误"
        print(f"测试用例{i+1}：输入={nums} | 预期={expected} | 实际={actual} | {status}")

if __name__ == "__main__":
    # nums = list(map(int, input().split()))
    # print(nums)
    # print(max_profit(nums))
    test_cases()
