class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map_one , map_two= {}, {}
        for ti in t: 
            if ti not in map_one:
                map_one[ti] =0
            map_one[ti] +=1

        def check_map(map_one:dict, map_two:dict):
            for key, values in map_one.items():
                if key not in map_two or values > map_two[key]:
                    return False
            return True
        left, right  = 0, len(s)
        min_length = float('inf')
        min_value = ''
        index = 0
        while left < right:
            if s[left] not in map_two:
                map_two[s[left]] =0
            map_two[s[left]] +=1     
            left+=1
            while check_map(map_one, map_two):
                if left-index < min_length:
                    min_value = s[index:left]
                    min_length = left-index
                map_two[s[index]] -=1
                if map_two[s[index]] == 0:
                    map_two.pop(s[index])
                index+=1
        return min_value

