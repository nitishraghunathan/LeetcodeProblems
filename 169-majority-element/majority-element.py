class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        tracker = None
        for element in nums:
            if count == 0:
                tracker = element
            count += -1 if element != tracker else 1
        return tracker
        