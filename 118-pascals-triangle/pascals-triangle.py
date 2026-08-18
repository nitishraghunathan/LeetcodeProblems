class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return []
        result = [[1]]
        for i in range(1, numRows):
            array = [1,1]
            for j in range(1, len(result[i-1])):
                array.insert(j, result[i-1][j-1] + result[i-1][j])
            result.append(list(array))
        return result


        