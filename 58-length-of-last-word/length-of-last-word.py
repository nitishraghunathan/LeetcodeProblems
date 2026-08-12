class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        right = len(s)-1
        if not s:
            return 0
        while right > 0 and s[right] != ' ':
            right-=1
        total = len(s) - right-1
        return total if right > 0 else total+1
        