class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_dict ={}
        result =[]
        for word in strs: 
            new_word = ''.join(sorted(word))
            if new_word not in map_dict:
                map_dict[new_word] = []
            map_dict[new_word].append(word)
        for key, value in map_dict.items():
            result.append(value)
        return result
