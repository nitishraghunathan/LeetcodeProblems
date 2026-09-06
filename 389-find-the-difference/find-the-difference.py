class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        map_dict = {}
        for index, value in enumerate(s):
            if value not in map_dict:
                map_dict[value] = 0
            map_dict[value] +=1
        for index, value in enumerate(t):
            if value not in map_dict:
                return value
            map_dict[value] -=1
            if map_dict[value] == 0:
                map_dict.pop(value)
        return ""


        