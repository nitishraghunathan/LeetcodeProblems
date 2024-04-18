class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs(queue, grid):
            directions = [[0,1],[0,-1],[-1,0],[1,0]]
            counter = -1
            while queue:
                size = len(queue)
                counter +=1
                for i in range(size):
                    direct = queue.pop(0)
                    for dir in directions:
                        x = dir[0] + direct[0]
                        y = dir[1] + direct[1]
                        if x < 0 or y < 0 or x > len(grid) -1 or y > len(grid[x])-1 or grid[x][y] !=1:
                            continue
                        grid[x][y]=2
                        queue.append((x,y))
            return counter
        value = 0
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2:
                    queue.append((i,j))
        value = bfs(queue, grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    return -1
        return 0 if value == -1 else value
        

