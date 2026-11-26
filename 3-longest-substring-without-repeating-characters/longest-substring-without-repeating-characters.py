class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map_dict, max_string = {}, 0
        left, index, right = 0, 0, len(s)
        while left < right:
            if s[left] not in map_dict:
                map_dict[s[left]] = left
                left+=1
                max_string = max(max_string, left-index)
            else:
                temp_index = map_dict[s[left]]
                while index <= temp_index and s[index] in map_dict:
                    map_dict.pop(s[index])
                    index+=1
                map_dict[s[left]] = left   
                left+=1
                
        return max_string
