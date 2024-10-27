class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_dict = {}
        for index,value in enumerate(nums):
            if target - value in map_dict:
                return [map_dict[target-value], index]
            if value not in map_dict:
                map_dict[value] = index

        return [-1, -1]

        