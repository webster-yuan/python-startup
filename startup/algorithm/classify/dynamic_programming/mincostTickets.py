import math
from typing import List


# https://leetcode.cn/problems/minimum-cost-for-tickets/
class Solution1:
    """
    使用DFS+枚举的方式计算，会存在大量的重复计算，如果在某个后续路径中再次遇到 cur_index=4 或 cur_index=1，
    就会 重复计算 f(4) 或 f(1)。
    例如在递归树里：

    f(0)
     ├─ 1天票 -> f(1)
     │        ├─ 1天票 -> f(2)
     │        ├─ 7天票 -> f(4)
     │        └─ 30天票 -> f(6)
     ├─ 7天票 -> f(4)
     └─ 30天票 -> f(6)

    f(4) 出现了两次
    f(6) 也出现了两次
    """
    durations = [1, 7, 30]

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        我需要一个函数，解决days[i...]之后需要的最少花费是多少，
        i 表示：现在要处理的旅行日的下标，也就是：从 days[i] 这天开始，你还没买票或没覆盖到它。
        """
        return self.get_min_cost_start_index(days, costs, 0)

    def get_min_cost_start_index(self, days: List[int], costs: List[int], cur_index: int) -> int:
        # 结束点：最后一天 len(days)-1 都已经规划过了，就无需额外花费了
        if cur_index == len(days):
            return 0

        ans = float('inf')  # 我们求最小花费，那就用无穷大
        # 枚举三种选择方式
        for k in range(len(costs)):
            # 找到这次选择之后，下一个应该旅行的日子，但是这个选择并没有覆盖到的日期
            next_index = cur_index
            while next_index < len(days) and days[cur_index] + self.durations[k] > days[next_index]:
                next_index += 1

            # 统计这次选择的花费，然后继续寻找下一个选择的最小花费
            ans = min(ans, costs[k] + self.get_min_cost_start_index(days, costs, next_index))

        return ans


class Solution2:
    """
    记忆化搜索的方式去掉重复计算，就是将之前计算过的cur_index=1的最佳选择记录下来，然后下次直接获取，避免重复计算
    递归 + 记忆化（memo）
    """
    # 类属性，所有的实例都会共享这一个数组
    durations = [1, 7, 30]

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        我需要一个函数，解决days[i...]之后需要的最少花费是多少，
        i 表示：现在要处理的旅行日的下标，也就是：从 days[i] 这天开始，你还没买票或没覆盖到它。
        """
        self.memo = {}  # 用于缓存 cur_index 的结果，需要时实例属性，否则会影响其他测试用例的结果
        return self.get_min_cost_start_index(days, costs, 0)

    def get_min_cost_start_index(self, days: List[int], costs: List[int], cur_index: int) -> int:
        # 结束点：最后一天 len(days)-1 都已经规划过了，就无需额外花费了
        if cur_index == len(days):
            return 0

        if cur_index in self.memo:
            return self.memo[cur_index]

        ans = float('inf')  # 我们求最小花费，那就用无穷大

        # 枚举三种选择方式
        for k in range(len(costs)):
            # 找到这次选择之后，下一个应该旅行的日子，但是这个选择并没有覆盖到的日期
            next_index = cur_index
            while next_index < len(days) and days[cur_index] + self.durations[k] > days[next_index]:
                next_index += 1

            # 统计这次选择的花费，然后继续寻找下一个选择的最小花费
            ans = min(ans, costs[k] + self.get_min_cost_start_index(days, costs, next_index))

        self.memo[cur_index] = ans
        return ans


class Solution3:
    """
    动态规划的方式：因为dp[0]依赖于dp[1]或者dp[7]或者dp[30]，是前面依赖后面的值，所以顺序是从后往前
    初始化dp[n]=0，就是DFS的退出条件
    """
    durations = [1, 7, 30]

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        k_range = len(costs)
        dp = [0] * (n + 1)  # 开辟n+1个空间，毕竟 n-1 这最后一天也是要纳入规划的
        dp[n] = 0
        for cur_index in range(n - 1, -1, -1):
            dp[cur_index] = float('inf')
            for k in range(k_range):
                next_index = cur_index
                while next_index < n and days[cur_index] + self.durations[k] > days[next_index]:
                    next_index += 1

                dp[cur_index] = min(dp[cur_index], costs[k] + dp[next_index])

        return dp[0]


if __name__ == '__main__':
    s = Solution3()
    print(s.mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]))
