class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        1. Iterate through the array
        2. Compute the sum at every index during the iteration.
        3. find the sum and well as the max_sum at that index
        """        
        max_sum = float('-inf')
        compute_sum = 0
        for index, value in enumerate(nums):
            compute_sum = max(compute_sum + value, value)
            max_sum = max(max_sum, compute_sum)
        return max_sum
