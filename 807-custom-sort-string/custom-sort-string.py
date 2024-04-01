class Solution:
    def customSortString(self, order: str, s: str) -> str:
        map_dict = {}
        for char in s:
            if char not in map_dict:
                map_dict[char] = 0
            map_dict[char] +=1
        result = []
        for ord in order:
            if ord in map_dict:
                result.append(ord*map_dict[ord])
                map_dict.pop(ord)
        for key, value in map_dict.items():
            result.append(key*value)
        return ''.join(result)
        