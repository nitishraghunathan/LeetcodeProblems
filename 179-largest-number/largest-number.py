class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums = sorted(nums, key = lambda a: a*10, reverse=True)
        return ''.join(nums) if nums[0]!='0' else '0'