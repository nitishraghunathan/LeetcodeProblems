class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_dict = {}
        for index,value in enumerate(nums):
            diff = target-value
            if diff in map_dict:
                return [map_dict[diff], index]
            else:
                map_dict[value] = index
        return [-1,-1]
            
        