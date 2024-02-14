class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 0:
            return -1.0
        if k > len(nums):
            return sum(nums)/len(nums)

        low = 0 
        high = k
        max_value = float('-inf')
        initial_sum = sum(nums[:k])
        max_value = max(max_value, initial_sum/k)
        for i in range(1, len(nums)-k+1):
            initial_sum += nums[i+k-1]
            initial_sum -= nums[i-1]
            max_value = max(max_value, initial_sum/k)
        return max_value
