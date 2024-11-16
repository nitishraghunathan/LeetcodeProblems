class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        To find the longest palindrome, we need to keep count with the number of alphabets, keys will the alphabets and values will be the occurences. 
        Maximum length of a palindrome is adding all the even occurences, and one odd occurence
        abdccdcdba
        """
        map_dict = {}
        for char in s:
            if char not in map_dict:
                map_dict[char] = 0
            map_dict[char] +=1
        even_count = 0
        odd_count = 0
        print(map_dict)
        odd_flag = False
        for key, value in map_dict.items():
            if value%2==0:
                even_count += value
            else:
                odd_flag = True
                odd_count += value -1
        return even_count + odd_count + 1 if odd_flag else even_count