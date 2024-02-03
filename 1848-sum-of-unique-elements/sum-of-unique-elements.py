class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        map_dict = {}
        unique_sum = 0
        for num in nums:
            if num not in map_dict:
                map_dict[num] = 0
            map_dict[num] +=1
        for key, value in map_dict.items():
            if value==1:
                unique_sum += key
        return unique_sum

