class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        counter = 1
        while True:
            if counter not in nums:
                return counter
            counter+=1
        