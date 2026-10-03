class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        map_dict = {}
        result = [-1,-1]
        for index, value in enumerate(nums):
            if value not in map_dict:
                map_dict[value] = 0
            map_dict[value] +=1
            if map_dict[value] == 2:
                result[0] = value 
        for i in range(1, len(nums)+1):
            if i not in map_dict:
                result[1] = i 
                return result
        return result
                
            

        