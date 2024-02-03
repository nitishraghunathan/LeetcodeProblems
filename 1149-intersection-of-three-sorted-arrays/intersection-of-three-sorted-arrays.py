class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        set_one = set(arr1)
        set_three = set(arr3)
        list1 = []
        list2 = []
        for val in arr2:
            if val in set_one:
                list1.append(val)
        
        for val in list1:
            if val in set_three:
                list2.append(val)
        return list2
        