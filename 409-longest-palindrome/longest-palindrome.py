class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Given a list of lowercase letters and uppercase letters, return the length of the longest palindrome that cna be built with those letters
        Aa
        AaA
        abccccdd
        What are the rules of palindrome:
        1. if length is even they should have same 6
        aabbcc
        we have a map of lowercase and upper case letters
        the longest length that can be formed
        abbba
        1. Get the count of alphabets in the string
        2. Determine those alphabets with an even count add them all
        3. Take any of the with max odd count and then return the answer

        """
        map_dict = {}
        for index,value in enumerate(s):
            if value not in map_dict:
                map_dict[value] = 0
            map_dict[value] += 1
        even_count_alphabets=0
        max_odd_count = 0
        odd_flag = False
        odd_count = 0
        for key, value in map_dict.items():
            if value%2==0:
                even_count_alphabets +=value
            else:
               odd_flag = True
               odd_count += value-1
        return even_count_alphabets + odd_count +1 if odd_flag else even_count_alphabets

        