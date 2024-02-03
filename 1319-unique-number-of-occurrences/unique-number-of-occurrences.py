class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map_dict={}
        occurences = set()
        for key in arr:
            if key not in map_dict:
                map_dict[key] = 0
            map_dict[key] +=1
        for key, value in map_dict.items():
            if value in occurences:
                return False
            occurences.add(value)
        return True