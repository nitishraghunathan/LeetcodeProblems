class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        max_val, second_max, index_one = -1, -1, -1
        for index, value in enumerate(nums):
            print(f"second_max: {second_max}, first_max = {max_val}")
            if value >= max_val:
                second_max, max_val = max_val, value
                index_one = index
            if value >= second_max and value < max_val:
                second_max=value
        return index_one if max_val >= 2* second_max else -1

        