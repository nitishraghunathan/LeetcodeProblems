class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_dict = {}
        for index, value in enumerate(s):
            if value not in map_dict:
                map_dict[value] = 0
            map_dict[value] +=1
        for index, value in enumerate(t):
            if value not in map_dict or map_dict[value] == 0:
                return False
            else:
                map_dict[value] -=1
        return True