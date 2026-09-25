class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        max_length = -1
        for i in range(max(len(a), len(b))):
            if a[:i] == b[:i]:
                continue
            else:
                max_length = i 
        return max_length+1 if max_length !=-1 else max_length
        
        