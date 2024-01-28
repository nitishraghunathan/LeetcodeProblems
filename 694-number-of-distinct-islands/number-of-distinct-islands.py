class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(i, j, string, value):
            if i < 0 or j < 0 or i > len(grid) -1 or j > len(grid[i])-1 or grid[i][j] != 1:
                return string
            grid[i][j] = -1
            string += value
            string = dfs(i+1, j, string, 'N')
            string = dfs(i-1, j, string, 'S')
            string = dfs(i, j+1, string, 'E')
            string = dfs(i, j-1, string, 'W')
            string += '0'
            return string

        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visited.add(dfs(i, j, '', 'start'))
        return len(visited)