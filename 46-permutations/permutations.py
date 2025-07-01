class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        """
        1. permutations to this problem
        recursion, pass in a parameter
            index, list and a result list
        """
        def define_permutations(nums, index):
            if index == len(nums):
                result.append(list(nums))
                return result
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                define_permutations(nums, index+1)
                nums[i], nums[index] = nums[index], nums[i]
            return result
        define_permutations(nums, 0)
        return result