class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        counter = -1
        def bfs(queue, grid):
            nonlocal counter
            directions = [[-1,0], [1,0], [0,1], [0,-1]]
            while queue:
                size = len(queue)
                for i in range(size):
                    x, y  = queue.pop(0)
                    for direct in directions:
                        new_x = x + direct[0]
                        new_y = y + direct[1]
                        if new_x < 0 or new_x > len(grid)-1 or new_y < 0 or new_y > len(grid[new_x])-1 or grid[new_x][new_y] !=1:
                            continue
                        queue.append([new_x, new_y])
                        grid[new_x][new_y] = 2
                counter +=1


        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append([i,j])
        bfs(queue, grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        return 0 if counter == -1 else counter