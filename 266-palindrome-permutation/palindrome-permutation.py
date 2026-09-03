class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        odd_count = 0
        map_dict = {}
        for index, value in enumerate(s):
            if value not in map_dict:
                map_dict[value] = 0
            map_dict[value] += 1
        for key, value in map_dict.items():
            if value%2 == 1:
                odd_count +=1
        return odd_count < 2 


        """
        Malayalam
        deed 
        carerac
        """
        
        