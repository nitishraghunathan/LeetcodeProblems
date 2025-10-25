class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []
        if not nums:
            return [[lower, upper]]
        if nums[0] - lower > 0:
            result.append([lower, nums[0]-1])
        for i in range(1, len(nums)):
             if nums[i] - nums[i-1] > 1:
                result.append([nums[i-1]+1, nums[i]-1])
        if upper - nums[-1] > 0:
            result.append([nums[-1]+1, upper])
        return result



        