class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## Two pointer Solution
        ## store characters in a map and keep track of the index. 
        ## when you encounter a repeating character
        ## get the index where the character last occured 
        ## store the last index where the substring began, remove all characters from there

        map_dict = {}
        string_begin = 0
        left = 0
        right = len(s)-1
        max_length = 0
        while left <= right:
            if s[left] not in map_dict:
                map_dict[s[left]] = left
                left +=1
                max_length = max(max_length, left-string_begin)
            else:
                old_char_index = map_dict[s[left]]
                while string_begin <= old_char_index:
                    map_dict.pop(s[string_begin])
                    string_begin +=1
                map_dict[s[left]] = left
                left+=1
        return max_length


                
                
                        
            