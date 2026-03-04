def RemoveDuplicateElementsV1():
    """
    T: O(nlogn)
    S: O(n)
    """
    list1 = [1,2,2,2,3,4,4,5,6,6,6,6,7,9]
    # 排序 O(NlogN)
    sorted_list = sorted(list1)
    print(f"排序之后的列表:{sorted_list}")

    # 统计每个数字的出现次数
    count_dict = {}
    for num in sorted_list:
        count_dict[num] = count_dict.get(num, 0) +1

    # 第二步:只保留出现次数为1的数字
    unique_only_list = [num for num in sorted_list if count_dict[num] == 1]
    print("只出现1次的数字:", unique_only_list)


def RemoveDuplicateElementsV2():
    """
    T:O(n)
    S:O(1)
    原地覆盖+截断列表:减少重复del影响效率
    """
    list1 = [1,2,2,2,3,4,4,5,6,6,6,6,7,9]
    nums = sorted(list1)
    n = len(nums)
    if n<=1:
        print("最终结果:",nums)
        return

    res_ptr = 0
    i =0 
    while i<n:
        # 找到当前数字的结束位置
        j = i
        while j<n and nums[j]==nums[i]:
            j+=1
        
        # 只保留出现1次的数字
        if j-i == 1:
            nums[res_ptr] = nums[i]
            res_ptr+=1
        
        # 跳过重复的数字,i直接跳到j的位置
        i=j
    
    del nums[res_ptr:]
    print("只出现1次的数字:",nums)


RemoveDuplicateElementsV1()
RemoveDuplicateElementsV2()


