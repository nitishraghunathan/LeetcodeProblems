class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        map_dict = {}
        for val in s:
            if val not in map_dict:
                map_dict[val] = 1
            else:
                map_dict[val] +=1
        counter = 0
        for value in map_dict.values():
            if value%2==1:
                if counter == 0:
                    counter +=1
                else:
                    return False
        return True
        