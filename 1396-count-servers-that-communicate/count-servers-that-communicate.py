class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_dict = [0]*len(grid)
        col_dict = [0]*len(grid[0])
        points = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    points.append((i,j))
                    row_dict[i] += 1
                    col_dict[j] +=1
        connected = 0
        for r,c in points:
            if row_dict[r] > 1 or col_dict[c] > 1:
                connected +=1
        return connected

        