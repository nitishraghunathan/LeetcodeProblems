class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map_dict = {0:-1}
        total_sum = 0
        max_value = 0
        for index, value in enumerate(nums):
            total_sum = total_sum +1 if value ==1 else total_sum-1
            if total_sum not in map_dict:
                map_dict[total_sum] = index
            else:
                max_value = max(max_value, index -  map_dict[total_sum])
        return max_value


