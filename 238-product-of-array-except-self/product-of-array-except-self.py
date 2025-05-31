class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        left_arr = [1]*size
        right_arr = [1]*size
        for i in range(1, size):
            left_arr[i] = left_arr[i-1]*nums[i-1]
        right = 1
        for i in range(size-1, -1, -1):
            left_arr[i] = left_arr[i]*right
            right*=nums[i]

        return left_arr


        