class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        We are given height of lines which span from zero at the Ith index to height[i].
        create a container which can stor maximum water based on area
        [1,8,6,2,5,4,8,3,7]
        In order to find the container compute the minimum height and distance between the left most pointer and right most pointer
        """
        max_area = float("-inf")
        min_height = float("inf")
        left = 0
        right = len(height) - 1
        while left <= right:
            min_height = min(height[left], height[right])
            max_area = max(max_area, min_height*(abs(left - right)))
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return max_area
