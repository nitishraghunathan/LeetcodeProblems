class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_dict = {}
        for index, value in enumerate(s):
            if value not in map_dict:
                map_dict[value] = 0
            map_dict[value] +=1
        for index, value in enumerate(t):
            if value not in map_dict:
                return False
            map_dict[value] -=1
            if map_dict[value] == 0:
                map_dict.pop(value)
        return not map_dict