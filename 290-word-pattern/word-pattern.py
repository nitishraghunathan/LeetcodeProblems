class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(s) != len(pattern):
            return False
        pattern_dict = {}
        for i in range(0, min(len(s), len(pattern))):
            if pattern[i] in pattern_dict and (pattern_dict[pattern[i]] != s[i]):
                return False
            if pattern[i] not in pattern_dict:
                if s[i] in set(pattern_dict.values()):
                    return False
                else:
                    pattern_dict[pattern[i]] = s[i]
        return True



        