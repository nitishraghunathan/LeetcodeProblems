class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1. Find the first left element less than its previous right element
        2. I findex greater than -1 find the smallest right element greater than the left element
        3. swap them and then reverse the string
        """
        left = len(nums) -2
        while left >-1 and nums[left] >=nums[left+1]:
            left -=1
        if left > -1:
            right = len(nums)-1
            while nums[left] >= nums[right]:
                right-=1
            nums[left], nums[right] = nums[right], nums[left]
        le = left +1
        ri = len(nums)-1
        while le <=ri:
            nums[le], nums[ri] = nums[ri], nums[le]
            le +=1
            ri -=1
        return nums
        