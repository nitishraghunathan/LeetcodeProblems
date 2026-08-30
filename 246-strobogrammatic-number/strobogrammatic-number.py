class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        map_dict = {
            "6" : "9",
            "8" : "8",
            "1" : "1",
            "9" : "6",
            "0" : "0"
        }
        if len(num) == 1:
            if num[0] in map_dict and map_dict[num[0]] == num[0]:
                return True
            else:
                return False
        left, right = 0, len(num) - 1
        while left <= right:
            if num[left] not in map_dict or map_dict[num[left]] != num[right]:
                return False
            right -= 1
            left +=1
        return True
        