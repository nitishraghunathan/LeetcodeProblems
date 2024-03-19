class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = float('-inf')
        for index, height in enumerate(heights):
            start_index = index 
            while stack and stack[-1][1] > height:
                old_index, old_height = stack.pop()
                max_area = max(max_area, (index-old_index)*old_height)
                start_index = old_index
            stack.append([start_index, height])
        for index, height in stack:
            max_area = max(max_area, height*(len(heights)-index))
        return max_area



