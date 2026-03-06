from typing import List

def numIslands(grid: List[List[str]]) -> int:
    """
    DFS
    """
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(row,col):
        if row<0 or row>=rows or col<0 or col>=cols or grid[row][col] == '0':
            return
        
        grid[row][col] = '0' # 标记为访问过
        
        dfs(row-1, col)
        dfs(row,col-1)
        dfs(row+1, col)
        dfs(row, col+1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j]=='1':
                dfs(i,j)
                count +=1
                dfs(i, j)

    return count

grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(numIslands(grid))  # 3