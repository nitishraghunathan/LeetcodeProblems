class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def recursion(nums, index, target, sum_value, result, fist):
            if sum_value == target:
                result.append(list(fist))
            if index == len(nums):
                return result

            result = recursion(nums, index+1, target, sum_value + nums[index], result, fist + [nums[index]])
            result = recursion(nums, index+1, target, sum_value, result, fist)
            return result
                

        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(1,len(dp)):
            for j in range(len(nums)):
                if nums[j] <= i:
                    dp[i] += dp[i-nums[j]]
        return dp[-1]