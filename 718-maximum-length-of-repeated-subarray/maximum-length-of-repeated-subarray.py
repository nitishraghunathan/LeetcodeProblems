class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0]*(len(nums2)+1) for i in range(len(nums1)+1)]
        max_value = 0
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    max_value = max(max_value, dp[i][j])
        return max_value