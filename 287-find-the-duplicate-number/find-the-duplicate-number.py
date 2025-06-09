class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Chose the index of the element - 1 and , if it is already negative it is duplicate
        """
        sum_array = sum(nums)
        for index, value in enumerate(nums):
            nums[abs(value)-1] = -nums[abs(value)-1]
            if nums[abs(value)-1] > 0:
                return abs(value)
        return -1
        