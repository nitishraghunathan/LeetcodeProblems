class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum%2 == 1:
            return False
        half_sum = total_sum//2
        dp = [False]*(half_sum+1)
        dp[0] = True
        for curr in nums:
            for j in range(half_sum, curr - 1, -1):
                dp[j] = dp[j] or dp[j - curr]
        print(dp)
        return dp[-1]