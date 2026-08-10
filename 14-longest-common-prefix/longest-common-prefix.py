class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        max_str = ""
        new_str = ""
        for char in strs[0]:
            max_str += char
            for i in range(1, len(strs)):
                if not strs[i].startswith(max_str):
                    return new_str
            new_str = max_str
        return new_str
        