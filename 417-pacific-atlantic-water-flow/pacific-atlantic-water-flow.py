class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Algorithm:

        Traverse rows closest to pacific and atlantic oceans till the grid coordinates whose height is less than the previous as we are moving in land. 
        Traverse columns closest to pacific and atlantic oceans till the grid coordinates whose height is less than the previous as we are moving in land. 

        add all the coordinates from pacific and atlantic to sets accordingly

        Find the coordinates found in both sets and then add them to the result

        """
        result = []
        pacific, atlantic = set(), set() 
        def dfs(row:int, col:int, visited:set, prev_height:int):
            if row < 0 or col <0 or row > len(heights) -1 or col > len(heights[0])-1 or heights[row][col] < prev_height or (row, col) in visited:
                return
            visited.add((row,col))
            dfs(row+1, col, visited, heights[row][col])
            dfs(row-1, col, visited, heights[row][col])
            dfs(row, col+1, visited, heights[row][col])
            dfs(row, col-1, visited, heights[row][col])
            return

        for r in range(len(heights)):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, len(heights[0])-1, atlantic, heights[r][len(heights[0])-1])
        
        for c in range(len(heights[0])):
            dfs(0, c, pacific, heights[0][c])
            dfs(len(heights)-1, c, atlantic, heights[len(heights)-1][c])
        
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i,j) in pacific and (i,j) in atlantic:
                    result.append([i,j])
        return result