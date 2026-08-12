class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for index, value in enumerate(nums):
            if value != val:
                nums[count] = value
                count +=1
        return count
        