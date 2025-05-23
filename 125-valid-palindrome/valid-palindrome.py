class Solution:
    def isPalindrome(self, s: str) -> bool:
        low,high = 0, len(s)-1
        while low < high:
            if s[low].lower() == s[high].lower():
                low+=1
                high-=1
            elif not s[low].isalnum():
                low +=1
            elif not s[high].isalnum():
                high-=1 
            else:
                return False
        return True


        