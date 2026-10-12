class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, index = 0, len(s),0
        max_len = 0
        map_dict = {}
        while left < right:
            letter = s[left]
            if letter in map_dict:
                new_index = map_dict[letter]
                while index <= new_index:
                    map_dict.pop(s[index])
                    index +=1
            map_dict[letter] = left
            left +=1
            max_len = max(max_len, left-index)
        return max_len

        