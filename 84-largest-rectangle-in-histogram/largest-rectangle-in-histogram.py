class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Algorithm:
        Initialize a stack
        1. add elements to the stack along with the index if elements are greater than the last element in the stack.
        2. otherwise
            a.if less than the stack then keep popping elements till the element is less than or equal to the last element in the stack
            b. Add the new element in the stack with index of the last element popped out to keep track of a new rectangle
            c. finally iterate the elements int eh stack and ifnd max area
        """
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
        
            


