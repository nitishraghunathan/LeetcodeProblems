class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        palindrome_str = str(x)
        left, right = 0, len(palindrome_str)-1
        while left < right:
            if palindrome_str[left] != palindrome_str[right]:
                return False
            left +=1
            right -=1
        return True
        