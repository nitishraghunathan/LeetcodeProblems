class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map_dict = {0:1}
        total_sum = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum += num 
            if prefix_sum - k in map_dict:
                total_sum += map_dict[prefix_sum-k]
            if prefix_sum not in map_dict:
                map_dict[prefix_sum] = 0
            map_dict[prefix_sum] +=1
        return total_sum
