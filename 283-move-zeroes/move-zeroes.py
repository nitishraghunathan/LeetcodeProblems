class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1. Take a pointer and keep track if element is zero is element is non zero replace the element at the pointers position.
        2. replace the remaining elements from 1st non zero position (pointer's position) with 0
        """
        count = 0
        for index, value in enumerate(nums):
            if value !=0:
                nums[count]=value
                count +=1
        for i in range(count, len(nums)):
            nums[i] = 0
        return nums
        