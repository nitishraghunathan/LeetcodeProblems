class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(result:list, nums:list, index):
            if index == len(nums):
                result.append(list(nums))
                return result
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                result = dfs(result, nums, index+1)
                nums[i], nums[index] = nums[index], nums[i]
            return result
        return dfs([], nums, 0)

            