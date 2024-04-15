class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map_dict = {0:-1}
        max_value = float('-inf')
        total_sum = 0
        for index, num in enumerate(nums):
            val = 1 if num == 1 else -1
            total_sum += val
            if total_sum not in map_dict:
                map_dict[total_sum] = index
            else:
                max_value = max(max_value, index-map_dict[total_sum])
        return 0 if max_value == float('-inf') else max_value