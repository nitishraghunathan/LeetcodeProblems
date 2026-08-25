class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        if len(nums) == len(set(nums)): return False
        for index, num in enumerate(nums): 
            if num in window: 
                return True
            window.add(num)
            if index >= k: 
                window.remove(nums[index-k])
        return False

        