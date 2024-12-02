class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = float('-inf')
        left, right = 0, len(height) - 1
        while left < right:
            max_area = max(max_area, min(height[left], height[right])*(right-left))
            if height[left] > height[right]:
                right -=1
            else:
                left +=1
        return max_area