class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums)-1
        new_array = [0]*len(nums)
        counter =len(nums)-1
        while left <= right:
            lsquare = nums[left]*nums[left]
            rsquare = nums[right]* nums[right]
            if rsquare >= lsquare:
                new_array[counter] = rsquare
                right-=1
                counter-=1
            else:
                new_array[counter] = lsquare
                left +=1
                counter-=1
        return new_array

