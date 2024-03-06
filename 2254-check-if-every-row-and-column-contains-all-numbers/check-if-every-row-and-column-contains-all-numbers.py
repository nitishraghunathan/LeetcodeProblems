class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            set_ray = set()
            for j in range(len(matrix[i])):
                set_ray.add(matrix[i][j]) 
            
            for i in range(1, len(matrix)+1):
                if i not in set_ray:
                    return False

        for j in range(len(matrix)):
            set_ray = set()
            for i in range(len(matrix)):
                set_ray.add(matrix[i][j]) 
            
            for i in range(1, len(matrix)+1):
                if i not in set_ray:
                    return False
        return True