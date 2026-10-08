class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        max_val = -1
        second_max = -1
        max_index = -1

        for index, value in enumerate(nums):
            if value > max_val:
                # Demote the old max to second_max
                second_max = max_val
                max_val = value
                max_index = index
            elif value > second_max:
                # Update second_max if value is between second_max and max_val
                second_max = value

        return max_index if max_val >= 2 * second_max else -1