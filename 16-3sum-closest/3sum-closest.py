class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        closest = float('inf')
        closest_sum = float('inf')
        for i in range(len(nums)):
            new_sum = nums[i]
            j= i+1
            k = len(nums)-1
            while j < len(nums)-1 and j < k:
                sum_three = new_sum + nums[j] + nums[k]
                diff = abs(target - sum_three)
                if diff < closest:
                    closest = diff
                    closest_sum = sum_three
                if sum_three > target:
                    k-=1
                else:
                    j+=1 
        return closest_sum

        