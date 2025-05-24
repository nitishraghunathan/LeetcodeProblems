class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map_dict = {}
        counter = 0
        for index,value in enumerate(nums):
            if value not in map_dict:
                map_dict[value] = 1
            else:
                return True
        return False
        