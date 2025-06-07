class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Using two pointers
        p0 - 0 
        p1 = len(nums)-1
        The algorithm is like follows:
        [2,0,2,1,1,0]
        while 0 - push right
        while 2 - push left
        while rig
        """
        def add_numbers(counter, left, number, nums):
            while counter > 0 and left < len(nums):
                nums[left] = number
                counter-=1
                left +=1
            return nums, left
        counter_zero = 0
        counter_one = 0
        counter_two = 0
        for index,value in enumerate(nums):
            if value == 0:
                counter_zero +=1
            elif value == 1:
                counter_one +=1
            else:
                counter_two +=1
        left = 0
        nums, left = add_numbers(counter_zero, left, 0, nums)
        nums, left = add_numbers(counter_one, left, 1, nums)
        nums, left = add_numbers(counter_two, left, 2, nums)
        return nums







        