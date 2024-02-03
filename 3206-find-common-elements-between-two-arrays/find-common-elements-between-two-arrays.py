class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_one = set(nums1)
        nums_two = set(nums2)
        count1 = 0
        count2 = 0
        for value1 in nums1:
            if value1 in nums_two:
                count1 +=1
        for value2 in nums2:
            if value2 in nums_one:
                count2 +=1
        return [count1, count2]