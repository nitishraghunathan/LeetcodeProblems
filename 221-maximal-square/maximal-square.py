class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        dp = {}
        max_value = 0
        rows = len(matrix)
        cols = len(matrix[0])
        
        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or matrix[r][c] == "0":
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            right = dfs(r, c + 1)
            diag = dfs(r + 1, c + 1)
            bot = dfs(r + 1, c)
            dp[(r,c)] = 1 + min(right, diag, bot)
            return dp[(r,c)]
            
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    max_value = max(max_value, dfs(r,c))
                    
        return max_value ** 2


