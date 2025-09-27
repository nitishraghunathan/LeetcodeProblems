class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_str = ""
        for i in range(min(len(word1), len(word2))):
            new_str += word1[i] + word2[i]
        if len(word1) > len(word2):
            new_str += word1[len(word2):]
        else:
            new_str += word2[len(word1):]
        return new_str
        