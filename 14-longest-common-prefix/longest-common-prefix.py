class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(0, len(strs[0])):
            prefix = strs[0][:i+1]
            for words in strs:
                if prefix != words[:i+1]:
                    return prefix[:i]
        return prefix

        