class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        1,0 -> 0,1 
        1,2 -> 2,1
        In order to do transpose of a matrix we need to increase the column counter to be 1 greatee then the row counte,r so that we dont do any repeatations 
        
        """
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])//2):
                matrix[i][j], matrix[i][len(matrix[i])-1-j] =  matrix[i][len(matrix[i])-1-j], matrix[i][j]
        return matrix