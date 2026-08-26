class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        Thought process:
        1. Two pointers - left and iterator - iterator moves till it finds the previous and current are not consecuritve once found appens the ranges to the list 
        """
        result = []
        left, iterator = 0, 0
        right = len(nums)
        while left < right:
            flag = False
            iterator = left +1
            while iterator < right and nums[iterator] - nums[iterator-1] == 1:
                iterator+=1
                flag = True
            if flag:
                result.append(f"{nums[left]}->{nums[iterator-1]}")
            else:
                result.append(f"{nums[left]}")
            left = iterator
        return result
        