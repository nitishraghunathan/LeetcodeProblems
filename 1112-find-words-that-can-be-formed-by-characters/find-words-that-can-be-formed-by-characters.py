class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        map_dict = {}
        for char in chars:
            if char not in map_dict:
                map_dict[char] = 0
            map_dict[char] += 1
        count = 0
        for word in words:
            new_map = map_dict.copy()
            flag = True
            for alpha in word:
                if alpha in new_map:
                    new_map[alpha] -=1
                    if  new_map[alpha] == 0:
                        new_map.pop(alpha)
                else:
                    flag = False
                    break
            if flag:
                count+=len(word)
        return count

