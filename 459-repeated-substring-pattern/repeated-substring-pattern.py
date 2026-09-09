class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        if length < 2:
            return False
        for i in range(1, (length//2) + 1):
            count = length//(i)
            multiple = s[:i]*count
            if multiple == s:
                return True
        return False

            


        