class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map_dict = {}
        for index, value in enumerate(magazine):
            if value not in map_dict:
                map_dict[value] = 0
            map_dict[value] += 1
        for index, value in enumerate(ransomNote):
            if value not in map_dict or map_dict[value] == 0:
                return False
            else:
                map_dict[value] -= 1
        return True