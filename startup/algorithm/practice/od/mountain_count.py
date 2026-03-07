def count_peeks(heights):
    """
    统计山峰数量
    """
    if not heights or len(heights) <= 1:
        return 0
    
    n = len(heights)
    count = 0
    for i in range(n):
        if i == 0:
            # 边界：只需大于右边
            if heights[i] > heights[i+1]:
                count += 1
            
        elif i==n-1:
            # 边界：只需大于左边
            if heights[i]>heights[i-1]:
                count +=1

        else:
            # 中间：需大于左右两边
            if heights[i]>heights[i-1] and heights[i]>heights[i+1]:
                count +=1

    return count

# 测试示例
input_str = "0,1,4,3,1,0,0,1,2,3,1,2,1,0"
heights = list(map(int, input_str.split(',')))
print(heights)
print(count_peeks(heights))  # 输出 3