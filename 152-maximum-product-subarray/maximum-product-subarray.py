class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        current_max, current_min = 1, 1
        for num in nums:
            if num ==0:
                current_max, current_min = 1, 1
                continue 
            result_max = current_max*num
            result_min = current_min*num
            current_max = max(num, result_max, result_min)
            current_min = min(num, result_min, result_max)
            result = max(result, current_max)
        return result
