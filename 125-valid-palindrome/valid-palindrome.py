class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
         1. check if the string reads the same forward and backward.
         2. we need to check only alphanumeric characters
         3. we also need to check if they are lowercase if not we convert them to lowercase
         4. Its more efficient to use two pointers
         5. we keep iterating the start pointer and the end pointer till we intersect.
         6. If we find an anomaly we return false else we conclude it is a palindrome
        """
        start = 0
        end = len(s)-1
        while start <= end:
            while  start < end and not s[start].isalnum():
                start+=1
            while start < end and not s[end].isalnum():
                end -=1
            if s[start].lower() != s[end].lower():
                return False
            start +=1
            end -=1
        return True