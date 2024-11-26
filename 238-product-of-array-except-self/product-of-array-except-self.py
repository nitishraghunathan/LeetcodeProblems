class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        left_array = [0]*size
        right_array = [0]*size
        result = [0]*size
        left_array[0] = nums[0]
        right_array[size-1] = nums[size-1]

        for i in range(1, size):
            left_array[i] = nums[i]*left_array[i-1]
        for j in range(len(nums)-2, -1, -1):
            right_array[j] = nums[j]*right_array[j+1] 
        for i in range(size):
            if i == 0:
                result[i] = right_array[i+1]
            elif i == len(nums) - 1:
                result[i] = left_array[i-1]
            else:
                result[i] = left_array[i-1]*right_array[i+1]
        return result
        