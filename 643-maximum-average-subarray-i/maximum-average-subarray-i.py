class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Step 1: Compute the sum of the first window of size k
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Step 2: Slide the window across the rest of the array
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
            
        # Step 3: Divide maximum sum by k using float division
        return max_sum / k