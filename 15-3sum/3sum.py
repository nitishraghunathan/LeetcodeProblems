class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        solution_set = []
        nums.sort()

        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]:
                continue
            if value > 0:
                break

            target = -value
            left, right = index + 1, len(nums) - 1

            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum > target:
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    solution_set.append([value, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return solution_set