class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(1,len(dp)):
            for j in range(len(nums)):
                if nums[j] <= i:
                    dp[i] += dp[i-nums[j]]
        return dp[-1]