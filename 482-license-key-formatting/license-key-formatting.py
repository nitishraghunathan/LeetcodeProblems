class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result = ""
        s = s.split("-")
        s = "".join(s)
        index = len(s)
        for i in range(len(s)-1,-1,-1):
            result = s[i].upper() + result
            if i > 0 and index-i==k:
                result = "-" + result
                index = i
        return result