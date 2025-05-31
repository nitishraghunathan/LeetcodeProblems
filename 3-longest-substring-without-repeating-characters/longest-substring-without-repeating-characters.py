class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = len(s)
        map_dict = {}
        index = 0
        max_length = 0
        while left < right:
            if s[left] not in map_dict:
                map_dict[s[left]] = left
                left +=1
                max_length = max(max_length, left-index)
            else:
                new_pointer = map_dict[s[left]]
                while index <= new_pointer:
                    map_dict.pop(s[index])
                    index +=1
                map_dict[s[left]] = left
                left+=1
        return max_length


        