from math import ceil
from typing import List


class Solution:
    """
    https://leetcode.cn/problems/koko-eating-bananas/submissions/693365029/
    """

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        一次吃最大值根，那么吃这一次肯定能把这堆香蕉吃完，那么小时数x只要保证<=h就可以了
        既然是为了求最小的速度speed=piles[index]/1，即k，就是为了确认可用区间的左边界k
        在[k,max_val]中，都是可以保证在h小时以内吃完的，就可以使用二分法确认
        那么我就需要一个函数，告诉我能不能在这个speed时，在h小时之内吃完，

        """
        left, right = 1, max(piles)
        ans = 0
        while left <= right:  # 当加一之后的left的值正好等于right，此时这个值还没有被判断，所以是 <=
            mid = left + (right - left) // 2  # 这里得保证整数除法，才能获取正确位置
            if self.is_enough(piles, mid, h):
                ans = mid
                right = mid - 1  # 因为这里我们记录的是ans，我们想继续尝试，所以变动一下，否则下次还是判断的当前值
            else:
                left = mid + 1

        return ans

    @classmethod
    def is_enough(cls, piles: list[int], speed: int, h: int) -> bool:
        """
        函数逻辑：一个小时只能吃一次，一次只能吃speed个，并且每桶香蕉还必须吃完，并且有剩下的时，下一次只能继续吃这一桶
        例子：piles = [3,6,7,11], h = 8
        我假设speed=4
        3/4=0，我吃一次就吃完了，一次就是一个小时，t+=1
        6/4=1，吃一次之后有剩下的，所以得再吃一次，t+=2
        7/4=1，吃一次之后有剩下的，所以得再吃一次，t+=2
        11/4=2，吃两次之后有剩下的，所以得再吃一次，t+=3
        1+2+2+3=8<=h=8，所以我可以吃完
        """
        count = 0
        for pile in piles:
            # 向上取
            # pile / speed 是浮点数除法，结果保留小数之后向上取整，pile=3, speed=2 → 3/2=1.5 → ceil(1.5)=2
            # pile // speed 是浮点数除法，结果去掉小数之后向上取整，pile=3, speed=2 → 3//2=1 → ceil(1)=1
            cost = ceil(pile / speed)
            count += cost

        return count <= h


if __name__ == '__main__':
    s = Solution()
    print(s.minEatingSpeed([30, 11, 23, 4, 20], 5))
    print(s.minEatingSpeed([30, 11, 23, 4, 20], 6))
    print(s.minEatingSpeed([3, 6, 7, 11], 8))
