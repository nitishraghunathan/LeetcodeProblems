class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, (len(matrix)*len(matrix[0]))-1
        while left <= right:
            mid = left + (right -left)//2
            value = matrix[mid//len(matrix[0])][mid%len(matrix[0])]
            if value == target:
                return True
            elif target > value:
                left = mid+1
            else:
                right = mid -1
        return False
        