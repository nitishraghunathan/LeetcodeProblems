class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        map_dict= {}
        max_value = float('-inf')
        for num in nums:
            if num not in map_dict:
                map_dict[num] =0
            map_dict[num]+=1
            max_value = max(max_value, map_dict[num])
        result = [[] for i in range(max_value)]
        for key, value in map_dict.items():
            for i in range(value):
                result[i].append(key)
        return result
