from typing import List


def monotonic_stack(nums: List[int]):
    # 每个元素 最多进栈一次、出栈一次
    # 总 push ≤ n
    # 总 pop ≤ n
    # → 整体 O(n)

    n = len(nums)
    left_min_index = [-1] * n
    right_min_index = [-1] * n

    stack = []

    for i in range(n):
        # 维护一个从低到顶（数组从0到n-1），是从小到大的顺序
        # 所以，数组stack的尾部元素就是单调栈的顶部
        stack_top_element_index = stack[-1]
        while stack and nums[i] < nums[stack_top_element_index]:
            # 如果发现这个元素比栈顶都小，就得弹出
            idx = stack.pop()
            # 弹出了，说明弹出的那个元素右侧第一个比他小的值就是当前这个元素，index=i
            right_min_index[idx] = i

        if stack:
            left_min_index[i] = stack_top_element_index

        stack.append(i)

    return left_min_index, right_min_index


if __name__ == '__main__':
    nums = [3, 7, 8, 4]
    left, right = monotonic_stack(nums)

    print(left)  # [-1, 0, 1, 0]
    print(right)  # [3, 3, 3, -1]
