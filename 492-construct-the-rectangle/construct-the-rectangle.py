class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        if area < 2:
            return [area, area]
        result = []
        length, width = 0, 0
        for i in range(1, (area // 2) + 1):
            if area % i == 0 and area // i >= i:
                length = area // i
                width = i
        result.append(length)
        result.append(width)
        return result
                
        