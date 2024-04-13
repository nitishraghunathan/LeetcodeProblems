class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Have a min value,
        use binary search 
        left = 0, right = len(arr)-1
        if number at left position is less than number at right position 
        that means it is a sorted array and left element hence we take the minimum of min value and left element
        else:
            we compute the middle value 
            if number at middle value is greater than number at position 0 
            left = mid+1
            else right = mid -1
        """
        left, right = 0, len(nums)-1
        min_value = float('inf')
        while left <= right:
            if nums[left] < nums[right]: 
                min_value = min(min_value, nums[left])
                return min_value
            mid = left + (right-left)//2
            min_value = min(min_value, nums[mid])
            if nums[mid]>=nums[0]:
                left = mid+1
            else:
                right = mid-1       
        return min_value