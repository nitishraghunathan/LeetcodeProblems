class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = set()
        """
        1. permutations to this problem
        recursion, pass in a parameter
            index, list and a result list
        """
        def define_permutations(nums, index):
            if index == len(nums):
                result.add(tuple(nums))
                return result
            for i in range(len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                define_permutations(nums, index+1)
                nums[i], nums[index] = nums[index], nums[i]
            return result
        define_permutations(nums, 0)
        return list(result)