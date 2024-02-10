class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        low = 0
        high = 1
        max_size = 1
        while high < len(nums):
            if nums[high] <= nums[high-1]:
                low = high
            else:
                max_size = max(max_size, high-low+1)
            high +=1
        return max_size
