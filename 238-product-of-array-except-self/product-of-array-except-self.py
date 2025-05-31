class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        left_arr = [1]*size
        right_arr = [1]*size
        for i in range(1, size):
            left_arr[i] = left_arr[i-1]*nums[i-1]

        for i in range(size-2, -1, -1):
            right_arr[i] = right_arr[i+1]*nums[i+1]
        nums[0] = right_arr[0]
        nums[-1] = left_arr[-1]
        for i in range(1, size-1):
            nums[i] = left_arr[i]*right_arr[i]
        return nums


        