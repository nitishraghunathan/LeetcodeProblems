class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        1. Have two pointer move frm each end and take the minimum height at each pointer to check water flow 
        2. Compute the maximum area 
        """
        left, right = 0, len(height)-1
        max_area = float('-inf')
        while left <= right:
            lheight, rheight = height[left], height[right]
            max_area = max(max_area, (right-left)*min(lheight,rheight))
            if lheight < rheight:
                left +=1
            else:
                right -=1
        return max_area

        