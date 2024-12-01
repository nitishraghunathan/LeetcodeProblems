class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        1. Take three pointers, zero, current, two. Zero and current would be at index 0 and two would be the last index of nums
        2. Iterate through all elements of the array from left to right
        3. when there is a zero value then swap elements at zero pointer and current pointer and increment both the pointers
        4. when there is a two value swap elements at current index and two pointer index, decrement two index
        5. if value is one then increment current index.
        """
        current, zero = 0,0
        two, right = len(nums) - 1, len(nums) -1 
        while current <= two:
            if nums[current] == 2:
                nums[current], nums[two] = nums[two], nums[current]
                two -=1
            elif nums[current] == 0:
                nums[current], nums[zero] = nums[zero], nums[current]
                current +=1
                zero+=1
            else:
                current +=1
        return nums        