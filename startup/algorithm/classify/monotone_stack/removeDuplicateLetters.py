from collections import deque, defaultdict, Counter


class Solution:
    # https://leetcode.cn/problems/remove-duplicate-letters/submissions/693642765/
    
    def removeDuplicateLetters(self, s: str) -> str:
        monotone_stack = deque()  # 大压小之后逆序完成最小字典序
        count = Counter(s)
        is_in_monotone_stack = set()

        for letter in s:
            # 什么时候将字符放入单调栈中？
            # 1. 没有出现过 2. 栈为空 3. 栈顶元素比自身字典序小

            # 什么情况下不直接将字符放到单调栈里面呢？
            # 1. 出现过 && 2. 栈不为空 && 3. 栈顶元素比自身字典序大
            # 就需要弹栈顶元素之后，再把当前的元素放到栈里面
            # 注意：弹出栈顶元素时，还需要后续是否还有这个元素，如果有，那么当前我可以放心弹掉

            count[letter] -= 1  # 每次进来减1，便于后续代码维护使用

            if letter in is_in_monotone_stack:  # 如果这个字符已经在栈中存在，栈中那个才是我们要的
                continue

            # 当元素是第一次出现的时候，就让他进来
            while len(monotone_stack) != 0 and monotone_stack[-1] > letter and count[monotone_stack[-1]] > 0:
                removed_letter = monotone_stack.pop()
                is_in_monotone_stack.remove(removed_letter)

            monotone_stack.append(letter)
            is_in_monotone_stack.add(letter)

        return "".join(monotone_stack)


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicateLetters("bcabc"))
    print(s.removeDuplicateLetters("cbacdcbc"))
