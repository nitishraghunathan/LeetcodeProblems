class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        new_arr = sorted(arr)
        rank = [0]*len(arr)
        map_dict = {}
        for index, number in enumerate(arr):
            if number not in map_dict:
                map_dict[number] = []
            map_dict[number].append(index)
        count = 0
        temp = float('-inf')
        for number in new_arr:
            if temp != number:
                count +=1
                temp=number
                for item in map_dict[number]:
                    rank[item] = count
        return rank