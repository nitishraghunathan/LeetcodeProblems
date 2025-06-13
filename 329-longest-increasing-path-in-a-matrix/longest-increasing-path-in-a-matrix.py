class Solution:
    """
        In order to find the longest increasing path in a 2d matrix we need to use the following tools:
        1. Iterating every element in the element in the matrix.
        2. Perform DFS + business logic to find the longest increasing path.
        3. Have a 2 dimensional array to cache the max path at each step.
    """
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_value = float('-inf')
        dp = [[-1]*len(matrix[0]) for i in range(len(matrix))]
        def dfs(matrix, i, j, prev):
            if i < 0 or j < 0 or i > len(matrix)-1 or j > len(matrix[i]) -1 or matrix[i][j] == -1 or matrix[i][j] <= prev:
                return 0
            if dp[i][j] !=-1:
                return dp[i][j]
            
            temp, matrix[i][j] = matrix[i][j], -1
            south = dfs(matrix, i+1,j, temp)
            north = dfs(matrix, i-1,j, temp)
            east = dfs(matrix, i,j+1, temp)
            west = dfs(matrix, i,j-1, temp)
            matrix[i][j] = temp
            dp[i][j] = 1 +max(north, max(south, max(east, west)))
            return dp[i][j]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                max_value = max(max_value, dfs(matrix,i,j, -1))
        return max_value