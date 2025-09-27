class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        size = len(s)
        for i in range(1, (size//2)+1):
            if size%i == 0:
                pattern = s[:i]*(size//i)
                if pattern == s:
                    return True
        return False

        