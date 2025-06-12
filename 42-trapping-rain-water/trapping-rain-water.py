class Solution:
    def trap(self, heights: List[int]) -> int:
        """
        We are going to use the two pointer approach.
            1. Left pointer and right pointers will be used, each pointing to the left end and right of the heights arrays.
            2. We compute the max height at each index the pointer is pointing, if left's height is greater than height then we compute rain water collected on the right side else we compute the rain water and left side
            3. The max height is constantly updated and the ocndition are evalauted till left meets right
        """
        left, right = 0, len(heights)-1
        left_max, right_max = float('-inf'), float('-inf')
        result = 0
        while left <= right:
            if left_max <= right_max:
                left_max = max(left_max, heights[left])
                result += left_max - heights[left]
                left +=1
            else:
                right_max = max(right_max, heights[right])
                result += right_max - heights[right]
                right -=1
        return result

        