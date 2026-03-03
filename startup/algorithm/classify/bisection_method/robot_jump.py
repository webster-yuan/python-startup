class Solution:
    # https://www.nowcoder.com/practice/7037a3d57bbd4336856b8e16a9cafd71

    def min_start_energy(self, heights: list[int]) -> int:
        left, right = 0, max(heights)
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2
            if self.is_enough_energy(heights, mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans

    @classmethod
    def is_enough_energy(cls, heights: list[int], start_energy: int) -> bool:
        cur_energy = start_energy
        for height in heights:
            cur_energy = 2 * cur_energy - height
            if cur_energy < 0:
                return False

        return True


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    # nums = [3, 4, 3, 2, 4]
    s = Solution()
    print(s.min_start_energy(nums))
