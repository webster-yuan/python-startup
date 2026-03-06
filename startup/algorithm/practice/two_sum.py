

def two_sum(nums: list[int], target:int):
    num_map={}
    for i , num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        
        num_map[num] = i

    return []

print(two_sum([2,7,5,8], 9))