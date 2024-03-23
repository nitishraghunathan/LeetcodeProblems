class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        def reverse(nums, low, high):
            while low < high:
                nums[low], nums[high] = nums[high], nums[low]
                low, high = low+1, high-1

            return nums
        nums = reverse(nums, 0, len(nums)-1)
        nums = reverse(nums, 0, k-1)
        nums = reverse(nums, k, len(nums)-1)
        return nums
        