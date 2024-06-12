class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs(queue, grid, counter):
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            while queue:
                size = len(queue)
                for i in range(size):
                    x, y = queue.pop(0)
                    for dir in directions:
                        x_new = x + dir[0]
                        y_new = y + dir[1]
                        if x_new < 0 or y_new < 0 or x_new > len(grid)-1 or y_new > len(grid[x_new]) -1 or grid[x_new][y_new] != 1:
                            continue
                        grid[x_new][y_new] = 2
                        queue.append([x_new, y_new])
                counter+=1
            return counter
        queue = []
        counter = -1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append([i,j])
        counter = bfs(queue, grid, counter)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        return 0 if counter == -1 else counter
                
