class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
       map_dict_one = {}
       map_dict_two = {}
       for tar in target:
           if tar not in map_dict_one:
               map_dict_one[tar] = 1
           else:
               map_dict_one[tar] +=1
       for tar in arr:
           if tar not in map_dict_two:
               map_dict_two[tar] = 1
           else:
               map_dict_two[tar] +=1
       return map_dict_one == map_dict_two