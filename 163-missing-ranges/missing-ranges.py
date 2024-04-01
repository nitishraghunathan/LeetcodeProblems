class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        
        if not nums:
            return [[lower, upper]]
        result = []
        if nums[0] > lower:
            result.append([lower, nums[0]-1])
        for index in range(len(nums)-1):
            if nums[index+1] - nums[index] > 1:
                result.append([nums[index]+1, nums[index+1]-1])
        if nums[-1] < upper:
            result.append([nums[-1]+1, upper])
        return result