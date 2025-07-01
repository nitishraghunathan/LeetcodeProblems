class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_dict = {}
        for i in range(len(s)):
            if s[i] not in map_dict and t[i] not in set(map_dict.values()):
                map_dict[s[i]] = t[i]
            elif t[i] != map_dict.get(s[i]):
                return False
        return True