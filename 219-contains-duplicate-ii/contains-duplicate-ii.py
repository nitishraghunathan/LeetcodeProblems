class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map_dict = {}
        for i in range(len(nums)):
            if nums[i] not in map_dict:
                map_dict[nums[i]] = []
                map_dict[nums[i]].append(i)
            else:
                for value in map_dict[nums[i]]:
                    if i - value <=k:
                        return True
                map_dict[nums[i]].append(i)
        return False