class Solution:
    def firstUniqChar(self, s: str) -> int:
        val = None
        indice = -1
        map_dict ={}
        for index, value in enumerate(s):
            if value not in map_dict:
                map_dict[value] = [1,index]
            else:
                map_dict[value][0] += 1
        for key, value in map_dict.items():
            if value[0]==1:
                if indice == -1:
                    indice = value[1]
                else:
                    indice = min(indice, value[1])
        return indice
            
        