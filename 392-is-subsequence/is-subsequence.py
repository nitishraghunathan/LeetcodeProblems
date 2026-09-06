class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        counter = 0
        for index, value in enumerate(t):
            if counter == len(s):
                return True
            if s[counter] == value:
                counter +=1
        return counter == len(s)