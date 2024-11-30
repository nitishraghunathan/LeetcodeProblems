class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = set()
        """
        1. Call the recursive function.
        2. have a for loop iterating through every element in the list 
        1, 2 ,3
        1, index +1
        2, index+1
        3, index +1

        if index == len(nums)
            add result.append(list(target))
        
        """
        def recursion(nums, index):
            if index == len(nums):
                result.add(tuple(nums))
                return
            for i in range(len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                recursion(nums, index+1)
                nums[index], nums[i] = nums[i], nums[index]
            return
        recursion(nums,0)
        return list(result)
        