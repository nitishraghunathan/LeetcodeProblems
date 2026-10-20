class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_dict = {}
        for word in strs:
            sorted_word  = "".join(sorted(word))
            if sorted_word not in map_dict:
                map_dict[sorted_word] = []
            map_dict[sorted_word].append(word)
        return [value for key, value in map_dict.items()]