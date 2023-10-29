class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        1. we get two occurences of all alphabets
        2. we get one occurence of only one alphabet buth two occurences of all other alphabets
        3. We would use the two pointer method 
        """
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1

            return True
        i = 0
        j = len(s) -1
        while i < j:
            if s[i] != s[j]:
                return check_palindrome(s, i, j-1) or check_palindrome(s, i + 1, j)
            
            i += 1
            j -= 1
        return True

        