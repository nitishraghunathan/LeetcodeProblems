class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums = sorted(nums)
        left, right = 0, len(nums)-1
        right_max = nums[-1]*nums[-2]*nums[-3]
        left_max = nums[0]*nums[1]*nums[-1]
        return max(right_max, left_max)
        