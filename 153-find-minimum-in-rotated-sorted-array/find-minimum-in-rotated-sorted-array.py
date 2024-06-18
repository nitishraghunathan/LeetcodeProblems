class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        min_value = float('inf')
        while left <= right:
            if nums[left] <= nums[right]:
                min_value = min(min_value, nums[left])
                return min_value 
            mid = left + (right-left)//2
            min_value = min(min_value, nums[mid])
            if nums[mid] >= nums[0]:
                left = mid+1
            else:
                right = mid-1
        return min_value