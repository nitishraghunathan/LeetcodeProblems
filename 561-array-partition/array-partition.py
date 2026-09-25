class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        total_sum = 0
        for i in range(0,len(nums)-1,2):
            total_sum += min(nums[i], nums[i+1])
        return total_sum
        