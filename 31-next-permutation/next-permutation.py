class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1. Find the first left element less than its previous right element
        2. I findex greater than -1 find the smallest right element greater than the left element
        3. swap them and then reverse the string
        """
        j = len(nums)-2
        while j > -1 and nums[j] >= nums[j+1]:
            j-=1
        if  j >-1:
            i= len(nums)-1
            while nums[j] >= nums[i]:
                i-=1
            nums[i], nums[j] = nums[j], nums[i]
        left = j+1
        right = len(nums)-1
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1
        return nums
        