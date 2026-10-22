class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()  # 1. Sort the array first
        
        for i in range(len(nums)):
            # Skip duplicate elements for the first position to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Use two pointers for the remaining part of the array
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum < 0:
                    left += 1  # We need a larger sum, move left pointer right
                elif current_sum > 0:
                    right -= 1 # We need a smaller sum, move right pointer left
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second and third elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
        return res