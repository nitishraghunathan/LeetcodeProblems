class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        min_value = float('inf')
        map_dict = {}
        def check_value(value):
            if len(value) > 1:
                total_sum = 0
                for i in value:
                     total_sum += i
                return total_sum
            return float('inf')


        for i in range(max(len(list1), len(list2))):
            if i < len(list1):
                if list1[i] not in map_dict:
                    map_dict[list1[i]] = []
                map_dict[list1[i]].append(i)
                min_value = min(min_value,check_value(map_dict[list1[i]]))
            if i < len(list2):
                if list2[i] not in map_dict:
                    map_dict[list2[i]] = []
                map_dict[list2[i]].append(i)
                min_value = min(min_value, check_value(map_dict[list2[i]]))
        result = []
        for index, value in map_dict.items():
            if check_value(value) == min_value:
                result.append(index)   
        return result         


        