class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 
        element = None 
        for i in nums:
            if count == 0:
                element = i
            count += -1 if i!= element else 1
        return element