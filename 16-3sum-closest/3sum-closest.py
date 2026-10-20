class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums = sorted(nums)
        min_diff = float('inf')
        closest_sum = float('inf')
        for index, i in enumerate(nums):
            left = index+1
            right = len(nums)-1
            while left < right and left!=index:
                total_sum = i+nums[left]+nums[right]
                diff = abs(target-total_sum)
                if diff < min_diff:
                    min_diff = min(min_diff,diff)
                    closest_sum = total_sum
                if total_sum > target:
                    right-=1
                else:
                    left+=1
        return closest_sum

        