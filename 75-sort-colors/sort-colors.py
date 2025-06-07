class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, first = 0, 0
        second = len(nums) - 1
        while first <= second:
            if nums[first] == 0:
                nums[first], nums[zero] = nums[zero], nums[first]
                zero +=1
                first+=1
            elif nums[first] == 2:
                nums[first], nums[second] = nums[second], nums[first]
                second -=1
            else:
                first+=1
        return nums