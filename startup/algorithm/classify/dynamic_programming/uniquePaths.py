# https://leetcode.cn/problems/unique-paths/description/

class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        递归
        """
        self.m = m
        self.n = n
        return self.dfs(0, 0)

    def dfs(self, row: int, col: int) -> int:
        """
        需要一个函数，告知我从(row,col)这个节点到(m,n)节点有多少种路径
        """
        # 划定范围
        if row == self.m - 1 and col == self.n - 1:
            return 1

        # 从当前节点，继续向下递归
        ret = 0
        if row + 1 < self.m:
            ret += self.dfs(row + 1, col)
        if col + 1 < self.n:
            ret += self.dfs(row, col + 1)

        return ret


class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        二维数组 正向dp 从起点
        dp[i][j] 表示从起点走到 (i, j) 的路径数
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
        """
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        二维数组 反向 dp 从终点，同 DFS 思路
        dp[i][j] 表示从 (i, j) 到达 (m-1,n-1) 位置的路径数
        dp[i][j] = dp[i+1][j] + dp[i][j+1]
        """
        dp = [[1] * n for _ in range(m)]
        for i in range(m - 2, -1, -1):  # range(起点, 终止(不包含), 步长)
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]


class Solution4:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        压缩为一维数组，因为(i,j)位置的值只取决于 (i,j-1) + (i-1,j) 的值
        (i,j-1)其实就是前一个位置的值，直接取 index -1 ，
        (i-1,j)其实就是上一个位置的值，其实就是一维数组里面的原值，
        数组向下滑动m行次，更新每一列，所以还是双层循环，只不过是空间缩为一维数组
        (i,j)新值就是 dp[j] = dp[j-1] + dp[j]
        """
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]

        return dp[n - 1]


if __name__ == '__main__':
    s = Solution4()
    print(s.uniquePaths(3, 7))
