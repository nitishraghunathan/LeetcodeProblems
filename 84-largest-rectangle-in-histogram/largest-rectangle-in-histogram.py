class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = float('-inf')
        for index, value in enumerate(heights):
            start_index = index
            while stack and stack[-1][1] > value:
                old_index, old_value = stack.pop()
                max_area = max(max_area, (index-old_index)*old_value)
                start_index = old_index
            stack.append([start_index, value])
        for index, value in enumerate(stack):
            max_area= max(max_area, value[1]*(len(heights)-value[0]))
        return max_area
            


