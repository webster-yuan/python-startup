# 搜索旋转排序数组

from typing import List

def search(nums: List[int], target: int) -> int:
    """
    二分查找： O(logN)
    """
    left, right = 0, len(nums)-1
    while left <=right:
        mid = left+(right-left)//2
        if nums[mid] == target:
            return mid
        
        # 左半部分有序
        if nums[mid] >= nums[left]:
            # 目标在左边
            if nums[mid] > target>=nums[left]:
                right = mid -1
            else:
                left = mid+1
        # 右半部分有序
        else:
            # 目标在右边
            if nums[mid] < target <= nums[right]:
                left = mid+1
            else:
                right = mid-1
        
    return -1


print(search([4,5,6,7,0,1,2], 0))  # 4
print(search([4,5,6,7,0,1,2], 3))  # -1
