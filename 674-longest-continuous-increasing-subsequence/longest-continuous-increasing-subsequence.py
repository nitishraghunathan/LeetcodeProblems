class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        left, index, max_length, right = 0,0,1, len(nums)
        while left < right:
            if left > 0 and nums[left] > nums[left-1]:
                max_length = max(max_length, left-index+1)
            else:
                index = left
            left+=1
        return max_length
        