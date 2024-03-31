class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ### Complete paths to finish line without hitting obstacles 
        ### This appears to be depth first search problem 
        ### We need store the state, can store it in a set or to be efficient we can just backtrack using grid by changing the matrix values from 0 to -1 
        ### the count the number of zeros, which will help us with our base case
        count_zero, start_row, start_col=0,0,0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    start_row = i
                    start_col = j
                if grid[i][j]==0:
                    count_zero +=1
        def dfs(grid, x, y, zeros):
            if x < 0 or x > len(grid)-1 or y <0 or y > len(grid[x])-1 or grid[x][y]==-1:
                return 0
            if grid[x][y]==2:
                return 1 if zeros ==-1 else 0
            grid[x][y] = -1
            total_distance = dfs(grid, x+1, y, zeros-1) + dfs(grid, x-1, y, zeros-1) + dfs(grid, x, y+1, zeros-1)   + dfs(grid, x, y-1, zeros-1)  
            grid[x][y]=0
            return total_distance   
        return dfs(grid, start_row, start_col, count_zero)