class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        def reverse(start, end, nums):
            while start < len(nums) and end > -1 and start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start +=1
                end -=1
            return nums
        nums = reverse(0, len(nums)-1, nums)
        nums = reverse(0, min(k-1, len(nums)-2), nums)
        nums = reverse(min(k, len(nums)-1), len(nums)-1, nums)
        return nums
        