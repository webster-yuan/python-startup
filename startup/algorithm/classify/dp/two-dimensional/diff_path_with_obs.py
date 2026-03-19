# https://leetcode.cn/problems/unique-paths-ii/description/
# 给定一个 m x n 的整数数组 grid。一个机器人初始位于 左上角（即 grid[0][0]）。机器人尝试移动到 右下角（即 grid[m - 1][n - 1]）。机器人每次只能向下或者向右移动一步。
# 网格中的障碍物和空位置分别用 1 和 0 来表示。机器人的移动路径中不能包含 任何 有障碍物的方格。
# 返回机器人能够到达右下角的不同路径数量。
# 测试用例保证答案小于等于 2 * 109。
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        状态定义： 我希望有个函数可以告诉我从(i,j)位置到达(m-1, n-1)位置有多少路径数
        初始化：dp[m-1][n-1] =1
        边界条件：if i ==m-1: res =dfs(i, j+1); if j == n-1:res=dfs(i+1, j)
        通用条件
        if obstacleGrid[i+1][j]==0 res =dfs(i, j+1)
        if obstacleGrid[i][j+1] == 0 res = dfs(i, j+1) 
        """
        m = len(obstacleGrid)
        n=len(obstacleGrid[0])
        
        memo = [[-1] * n for _ in range(m+1)]
        
        def memo_dfs(i,j):
            if i >= m or j >=n or obstacleGrid[i][j] ==1:
                return 0
            
            if i == m-1 and j == n-1:
                return 1
            
            if memo[i][j] !=-1:
                return memo[i][j]

            res = 0 
            res +=memo_dfs(i+1,j)
            res +=memo_dfs(i,j+1)
            memo[i][j] =res
            return res

        return memo_dfs(0,0)
    

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        状态定义： 我希望有个函数可以告诉我从(i,j)位置到达(m-1, n-1)位置有多少路径数
        初始化：dp[m-1][n-1] =1
        边界条件：if i ==m-1: res =dfs(i, j+1); if j == n-1:res=dfs(i+1, j)
        通用条件
        if obstacleGrid[i+1][j]==0 res =dfs(i, j+1)
        if obstacleGrid[i][j+1] == 0 res = dfs(i, j+1)

        转变思路： 将非法的路径都直接返回，剩下的直接加上就可以了

        ->dp
        状态定义：dp[i][j] 代表的就是从(i,j)位置到达(m-1,n-1)位置可能到达的路径个数
        初始化：dp[m-1][n-1] = 1
        最后一列，最后一行需要都定义为1，
        因为这里存在障碍物，所以可以多开一行多开一列，都为0
        状态转移：左依赖于右，从右往左推；上依赖于下，从下往上推；
        所以在右边和下边多开一行多开一列，
        返回值就是dp[0][0]，从原始起点到达终点(m-1,n-1)位置的路径个数
        初始化：第一行，第一列都为0， 这样从dp[0][0]到dp[1][1]的路径个数为0
        将整个数组融入到整体逻辑里面

        """
        m = len(obstacleGrid)
        n=len(obstacleGrid[0])

        dp = [[0] * (n+1) for _ in range(m+1)]
        if obstacleGrid[m-1][n-1] ==0:
            dp[m-1][n-1] = 1

        for i in range(m-1, -1,-1):
            for j in range(n-1, -1,-1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] =0
                    continue

                # 避免覆盖正确值
                if i ==m-1 and j ==n-1:
                    continue

                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        
        return dp[0][0]