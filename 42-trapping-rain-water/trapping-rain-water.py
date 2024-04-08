class Solution:
    def trap(self, height: List[int]) -> int:
        """
        1. Find min of left max and right max 
        2. how do we do that ?
        if left is less than right 
        and left_max <=rightmax 
        we compute new left max and subtract height at that position and give it back
        """
        if not height or len(height) < 2:
            return 0
        left, right = 0, len(height)-1
        left_max = float('-inf')
        right_max = float('-inf')
        result = 0
        while left <=right:
            if left_max <= right_max:
                left_max = max(left_max, height[left])
                result += left_max -height[left]
                left+=1
            else:
                right_max = max(right_max, height[right])
                result+= right_max - height[right]
                right-=1
        return result