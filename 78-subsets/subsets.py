class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = set()
        def subset(nums, subset_combination, index):
            nonlocal result
            if index == len(nums):
                result.add(tuple(subset_combination))
                return result
            for i in range(index, len(nums)):
                subset_combination.append(nums[i])
                result = subset(nums, list(subset_combination), i+1)
                subset_combination.pop()
                result = subset(nums, list(subset_combination), i+1)
            return result
        result = subset(nums, [], 0)
        return [list(iters) for iters in result]

        