class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*(len(nums))
        product = 1
        result[0] = nums[0]
        for i in range(1, len(nums)):
            product *= nums[i-1]
            result[i] = product
        product = 1
        for j in range(len(nums)-2, -1, -1):
            product *= nums[j+1]
            if j == 0:
                result[j] = product
            else:
                result[j] *= product
        return result
