class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        1. Expand around the centres to find the longest palindromic substring
        2. Odd length palindromes and even length palindromes 
        """
        max_length = 0
        max_length_string = ""
        def palindrome_length(c1: int, c2: int, s: str):
            left, right = c1, c2
            while left > -1 and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        for index, value in enumerate(s):
            single_center = palindrome_length(index, index,s)
            double_center = palindrome_length(index, index+1, s)
            if len(single_center) > max_length:
                max_length = len(single_center)
                max_length_string = single_center
            if len(double_center) > max_length:
                max_length = len(double_center)
                max_length_string = double_center
        return max_length_string
        