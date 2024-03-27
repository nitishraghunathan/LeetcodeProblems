class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = (len(matrix)*len(matrix[0]))-1
        while left <= right:
            mid = left + (right-left)//2
            pivot_mid = matrix[mid//len(matrix[0])][mid%(len(matrix[0]))]
            if pivot_mid==target:
                return True
            elif pivot_mid > target:
                right = mid-1
            else:
                left = mid+1
        return False