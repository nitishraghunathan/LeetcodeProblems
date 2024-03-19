class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = float('-inf')
        for index, value in enumerate(heights):
            start_index = index 
            while stack and stack[-1][1] > value:
                oi, ov = stack.pop()
                max_area = max(max_area, ov*(index-oi))
                start_index=oi
            stack.append([start_index, value])
        for index ,value in enumerate(stack):
            max_area = max(max_area, value[1]*(len(heights)-value[0]))
        return max_area
        
            


