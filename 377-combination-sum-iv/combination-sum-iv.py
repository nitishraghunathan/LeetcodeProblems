class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(1, len(dp)):
            for j, num in enumerate(nums):
                if num <= i:
                    dp[i] += dp[i - num]
        return dp[-1]