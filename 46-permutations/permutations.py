class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = set()
        def recursion(nums, start):
            if start > len(nums)-1:
                return result
            result.add(tuple(nums))
            for i in range(0, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                recursion(nums, start+1)
                nums[start], nums[i] = nums[i], nums[start]
            return result
        return list(recursion(nums, 0))
