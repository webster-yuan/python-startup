# 数组原地去重,返回去重后的长度, 不使用额外空间
def remove_duplicates(nums):
    if not nums:
        return 0
    
    slow = 0
    for fast in range(1, len(nums)):
        if nums[slow]!=nums[fast]:
            slow +=1
            nums[slow] = nums[fast]
    
    return slow + 1

if __name__ == "__main__":
    nums = [1,1,2]
    length = remove_duplicates(nums)
    print(length)  # 2
    print(nums[:length])  # [1,2]

    nums = [0,0,1,1,1,2,2,3,3,4]
    length = remove_duplicates(nums)
    print(length)  # 5
    print(nums[:length])  # [0,1,2,3,4]