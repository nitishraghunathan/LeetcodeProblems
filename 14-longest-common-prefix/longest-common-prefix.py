class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not str:
            return ''

        prefix = ''
        for i in range(len(strs[0])):
            prefix +=strs[0][i]
            for j in range(1, len(strs)):
                if prefix != strs[j][:i+1]:
                    return strs[j][:i]
        return prefix