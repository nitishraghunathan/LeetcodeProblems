class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for index, value in enumerate(nums):
            if value !=0:
                nums[count]=value
                count+=1
        for i in range(count, len(nums)):
            nums[i]=0
        return nums