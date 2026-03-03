from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 0, sum(batteries)
        ans = 0
        # T = n * log(N)
        while left <= right:  # T = log(N)
            mid = left + (right - left) // 2
            if self.is_enough(mid, batteries, n):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans

    @classmethod
    def is_enough(cls, mid, batteries, n) -> bool:
        # 缺少条件：就是同一时间，一个电池不能拆分给到另外的电脑
        # 所以sum_of_batteries = sum(batteries)过于宽松，就暗含了缺少的条件应该默认满足导致出错
        # 一台电脑期望运行mid分钟，比他大的就拿mid分钟，比他小的就拿小的分钟数，
        # 最后求的和作为判定条件才是真实满足实际情况的，小的几个可以拆分换着来
        # 大的肯定是满足的，拿mid，保证缺少的条件满足，代表的意思就是没有多余电量给到别的电脑
        # 即不能拆分出来，同时供电
        # T = O(n)
        sum_of_batteries = sum([min(b, mid) for b in batteries])
        if sum_of_batteries < mid * n:
            return False
        else:
            return True


if __name__ == '__main__':
    s = Solution()
    print(s.maxRunTime(3, [10, 10, 3, 5]))

    print(s.maxRunTime(2, [3, 3, 3]))
    print(s.maxRunTime(2, [1, 1, 1, 1]))
