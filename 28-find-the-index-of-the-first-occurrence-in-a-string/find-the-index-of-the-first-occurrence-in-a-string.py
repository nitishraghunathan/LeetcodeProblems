class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack or not needle:
            return 0
        length  = len(needle)
        for index, value in enumerate(haystack):
            if value == needle[0] and haystack[index:index+length] == needle:
                return index

        return -1
        