class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map_dict = {}
        for index, value in enumerate(nums):
            if value not in map_dict:
                map_dict[value] = []
            map_dict[value].append(index)
            new_list = map_dict[value]
            for i in range(1, len(map_dict[value])):
                if abs(new_list[i] - new_list[i-1]) <= k:
                    return True
        return False

        