class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map_dict = {}
        max_length = 0
        tracker = 0
        for index, character in enumerate(s):
            if character not in map_dict:
                map_dict[character] = index
                max_length = max(max_length, len(map_dict))
            else:
                old_index = map_dict[character]
                while tracker <= old_index:
                    map_dict.pop(s[tracker])
                    tracker +=1
                map_dict[character] = index
        return max_length
            

        