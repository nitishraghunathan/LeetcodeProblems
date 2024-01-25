class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i, j, value):
            if i < 0 or i > len(grid) -1 or j < 0 or j > len(grid[i]) -1 or grid[i][j] != 1:
                return 0
            grid[i][j] = value
            return 1 + dfs(i+1, j, value) + dfs(i-1, j, value) + dfs(i, j+1, value) + dfs(i, j-1, value)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i == 0 or i == len(grid) -1 or j == 0 or j == len(grid[i])-1) and grid[i][j]==1:
                    val = dfs(i, j, -1)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    count += dfs(i, j , -1)
        return count
