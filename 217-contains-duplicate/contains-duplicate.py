class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_new = set()
        for i in nums:
            if i in set_new:
                return True
            set_new.add(i)
        return False
        