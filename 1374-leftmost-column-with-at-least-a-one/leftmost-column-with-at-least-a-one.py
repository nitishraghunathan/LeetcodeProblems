class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        row, col = 0, cols - 1
        leftmost = -1
        
        while row < rows and col >= 0:
            if binaryMatrix.get(row, col) == 1:
                leftmost = col  # Update answer
                col -= 1        # Try to find a more left 1
            else:
                row += 1        # Move to next row if current is 0
        
        return leftmost
