class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n, result = len(matrix), len(matrix[0]), 0
        dp = [0]*n  # 1D array
        for i in range(m):
            prev = 0  # stores dp[i-1][j-1]
            for j in range(n):
                dp[j], prev = 0 if matrix[i][j] == '0' else \
                    (min(dp[j],  # dp[j] -> dp[i-1][j]
                         dp[j-1] if j > 0 else 0,  # dp[j-1] -> dp[i][j-1]
                         prev)  # prev -> dp[i-1][j-1]
                    + 1), dp[j]
                result = dp[j] if dp[j] > result else result
        return result*result