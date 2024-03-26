class Solution:
    def reorganizeString(self, s: str) -> str:
        adjacent_count = 0
        adjacent_character = None
        map_dict = {}
        for character in s:
            if character not in map_dict:
                map_dict[character] = 0
            map_dict[character] +=1
            if not adjacent_character or character != adjacent_character:
                adjacent_character = character
            else:
                adjacent_count +=1
        result= []
        heapq.heapify(result)
        for key, value in map_dict.items():
            heapq.heappush(result, (-value, ord(key)))
        new_string = ''
        while len(result) > 1:
            value1, key1 = heapq.heappop(result)
            value2, key2 = heapq.heappop(result)
            new_string += chr(key1) +chr(key2)
            if value1 +1 != 0:
                heapq.heappush(result, (value1+1, key1))
            if value2 + 1 !=0:
                heapq.heappush(result, (value2+1, key2))
        if result:
            value , key = heapq.heappop(result)
            new_string += chr(key)
            if value+1 !=0:
                return ''
        return new_string


