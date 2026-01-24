from typing import List


# https://leetcode.cn/problems/unique-paths-ii/description/
class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.m = len(obstacleGrid)
        self.n = len(obstacleGrid[0])
        return self.dfs(obstacleGrid, 0, 0)

    def dfs(self, obstacleGrid: List[List[int]], row: int, col: int) -> int:
        if obstacleGrid[row][col] == 1:
            # 特殊规则：起点就是不能走，那就只有0条路径
            return 0

        if row == self.m - 1 and col == self.n - 1:
            # 正常结束条件：到达最后一个位置
            return 1

        ret = 0
        if row + 1 < self.m and obstacleGrid[row + 1][col] == 0:
            ret += self.dfs(obstacleGrid, row + 1, col)

        if col + 1 < self.n and obstacleGrid[row][col + 1] == 0:
            ret += self.dfs(obstacleGrid, row, col + 1)

        return ret


class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        正向dp，在左边和上边多开一行多开一列，避免起点就是1（不可达），这样将
        游戏规则融入到整体的计算中，不再进行单独判断
        dp[i][j] 表示：在递推规则约束下，从“逻辑起点”走到 (i,j) 的路径数
        逻辑起点 ≠ 物理网格的 (0,0)
        逻辑起点是：dp[0][1]
        多加的一行一列并不代表物理真实网格情况，只是逻辑起点，-> 哨兵行列
        为了让物理真实网格记录情况属实，即逻辑上的dp[1][1]这个obs[0][0]起点到起点的路径只有1真实存在，
        并且满足dp[i][j] = dp[i - 1][j] + dp[i][j - 1]，才需要开个口子
        dp[i - 1][j] = 1 或者 dp[i][j - 1]
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if obstacleGrid[i - 1][j - 1] == 0:  # 多加一行一列，用下标回访原数组时注意-1
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m][n]


if __name__ == '__main__':
    s = Solution2()
    obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(s.uniquePathsWithObstacles(obstacleGrid))
