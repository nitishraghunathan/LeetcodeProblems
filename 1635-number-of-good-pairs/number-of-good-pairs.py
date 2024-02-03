class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        map_dict = {}
        count = 0
        for index, value in enumerate(nums):
            if value not in map_dict:
                map_dict[value] = []
            if len(map_dict[value]) > 0:
                count += len(map_dict[value]) 
            map_dict[value].append(index)
        return count

        return count