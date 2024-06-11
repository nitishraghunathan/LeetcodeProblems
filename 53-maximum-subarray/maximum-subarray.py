class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        max_num = float('-inf')
        for num in nums:
            max_num = max(max_num+num, num)
            max_sum = max(max_sum, max_num)
        return max_sum
            
        