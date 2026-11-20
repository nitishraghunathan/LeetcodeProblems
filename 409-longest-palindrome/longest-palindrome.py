class Solution:
    def longestPalindrome(self, s: str) -> int:
        map_dict = {}
        for index, value in enumerate(s):
            if value not in map_dict:
                map_dict[value] = 0
            map_dict[value] +=1

        odd_count, even_count, flag = 0, 0, False
        for key, value in map_dict.items():
            if value%2 == 1:
                if not flag:
                    flag =True
                    odd_count+=value
                else:
                    odd_count += (value-1)
            else:
                even_count+=value
        return even_count+odd_count