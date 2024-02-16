class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result = []
        max_value = float('-inf')
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > max_value:
                result.insert(0,i)
                max_value = heights[i]
        return result