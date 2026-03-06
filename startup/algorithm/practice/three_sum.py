def threeSum(nums: list[int]) -> list[list[int]]:
    """
    去重+双指针： 遍历一遍 O(N) 双指针针对每个元素又遍历一遍，所以是O(N^2)
    """
    nums.sort()
    res = []
    n= len(nums)
    for i in range(n):
        # 特殊情况处理
        # 固定的第一个数和前面的一个数相同，就没必要再找了 ，直接跳过
        # 因为肯定被双指针处理过了
        if i>0 and nums[i-1] == nums[i]:
            continue

        left , right= i+1, n-1
        while left < right:
            total = nums[i]+nums[left]+nums[right]
            if total < 0:
                left +=1
            elif total >0:
                right -=1
            else:
                # 先把理想结果记录下来
                res.append([nums[i], nums[left], nums[right]])

                # 去掉重复组合
                while left<right and nums[left] == nums[left+1]:
                    left +=1
                
                while left <right and nums[right] == nums[right-1]:
                    right -=1
                
                left +=1
                right -=1
    
    return res

print(threeSum([-1,0,1,2,-1,-4]))