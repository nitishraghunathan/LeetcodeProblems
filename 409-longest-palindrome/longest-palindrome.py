class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        To find the longest palindrome, we need to keep count with the number of alphabets, keys will the alphabets and values will be the occurences. 
        Maximum length of a palindrome is adding all the even occurences, and one odd occurence
        abdccdcdba
        """
        repeated_occurences = set()
        for char in s:
            if char not in repeated_occurences:
                repeated_occurences.add(char)
            else:
                repeated_occurences.remove(char)
        return len(s) - len(repeated_occurences) + 1 if len(repeated_occurences) > 0 else len(s)