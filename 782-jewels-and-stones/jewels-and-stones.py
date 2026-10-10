class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        map_dict = {}
        for jewel in jewels:
            if jewel not in map_dict:
                map_dict[jewel] = 0
            map_dict[jewel] +=1
        counter = 0
        for stone in stones:
            if stone in map_dict:
                counter+=1
        return counter
        
        