class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for value in nums:
            if nums[abs(value)-1] < 0:
                result.append(abs(value))
            else:
                nums[abs(value)-1] = -nums[abs(value)-1]
        return result
