class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(start, end):
            while start < end:
                if s[start]!= s[end]:
                    return False
                start +=1
                end-=1
            return True
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return check_palindrome(left, right-1) or check_palindrome(left+1, right)
            left +=1
            right-=1
        return True
        