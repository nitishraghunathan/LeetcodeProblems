class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(0,len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == '1':
                    self.dfs(grid,i,j)
                    count +=1
                       
        return count
    def dfs(self, grid: List[List[str]], i : int, j:int):
        if i < 0 or j < 0 or i > len(grid) -1 or j > len(grid[i]) -1 or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        return