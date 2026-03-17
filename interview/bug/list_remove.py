nums = [1,2,3,4,6,7]
for num in nums:
    if num % 2 == 0:
        """
        永远不要在遍历 list 时修改它本身。# 期望输出: [1, 3, 5, 7]
        """
        nums.remove(num)  # 迭代时删除元素

print(nums)  # 实际输出：[1, 3, 6, 7]