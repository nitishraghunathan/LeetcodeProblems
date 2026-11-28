class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        solution_set = []
        nums = sorted(nums)
        map_dict = set()
        for index, value in enumerate(nums):
            target = -value
            left,right = index+1, len(nums)-1
            while left < right:
                if nums[left] + nums[right] > target:
                    right -=1
                elif nums[left] + nums[right] == target:
                    left_val = nums[left]
                    right_val = nums[right]
                    key = tuple([value, left_val,right_val])
                    if key not in map_dict:
                        map_dict.add(key)
                        solution_set.append([value, left_val, right_val])
                    left +=1
                    right -=1
                else:
                    left+=1
        return solution_set
                    
        