class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []
        result = [[1]]
        for i in range(1, 34):
            array = [1,1]
            for j in range(1, len(result[i-1])):
                array.insert(j, result[i-1][j-1] + result[i-1][j])
            result.append(list(array))
        return result[rowIndex]
