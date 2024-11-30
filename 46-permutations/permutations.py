class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
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
        tracking_set = set()
        def recursion(nums, index, target_list):
            if len(target_list) == len(nums):
                result.append(list(target_list))
                return
            for i in range(len(nums)):
                if nums[i] not in tracking_set:
                    tracking_set.add(nums[i])
                    target_list.append(nums[i])
                    recursion(nums, i, target_list)
                    target_list.pop()
                    tracking_set.remove(nums[i])
            return
        recursion(nums,0,[])
        return result
        