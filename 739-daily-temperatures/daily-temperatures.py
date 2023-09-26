class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for index, value in enumerate(temperatures):
            while stack and stack[-1][1] < value:
                ind, val = stack.pop()
                result[ind] = index-ind
            stack.append([index, value])
        return result