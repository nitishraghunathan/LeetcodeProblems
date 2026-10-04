class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        map_dict = {}
        max_count, max_value = float('-inf'), float('-inf')
        min_length = float('inf')
        for index, num in enumerate(nums):
            if num not in map_dict:
                map_dict[num] = []
            map_dict[num].append(index)
            if len(map_dict[num]) >= max_count:
                max_count = len(map_dict[num])
        for key, value in map_dict.items():
            if len(value) == max_count:
                min_length = min(value[-1]-value[0]+1, min_length)
        return  min_length
