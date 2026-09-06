class Solution:
    def longestPalindrome(self, s: str) -> int:
        map_dict = {}
        for index, value in enumerate(s):
            if value not in map_dict:
                map_dict[value] = 0
            map_dict[value] +=1
        odd_flag, odd_count, even_count = False, 0,0
        for key, value in map_dict.items():
            if value%2==0:
                even_count +=value
            else:
                odd_flag = True
                odd_count += value-1
        return even_count if not odd_flag else odd_count+even_count+1
        
        