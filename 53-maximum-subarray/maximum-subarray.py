class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        current_sum, max_sum = float('-inf'),float('-inf')
        for i in nums:
            current_sum = max(i, i+current_sum)
            max_sum = max(current_sum, max_sum)
        return max_sum
