class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        map_dict = {}
        for r, rows in enumerate(matrix):
            for c, cols in enumerate(matrix[r]):
                if r-c not in map_dict:
                    map_dict[r-c] = cols
                else:
                    if map_dict[r-c] != cols:
                        return False
        return True

