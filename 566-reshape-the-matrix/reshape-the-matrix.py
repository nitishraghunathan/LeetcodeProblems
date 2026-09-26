class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        # Check if reshape is possible
        if m * n != r * c:
            return mat
            
        res = [[0] * c for _ in range(r)]
        rcount, ccount = 0, 0
        
        for i in range(m):
            for j in range(n):
                res[rcount][ccount] = mat[i][j]
                ccount += 1
                if ccount == c:
                    ccount = 0
                    rcount += 1
                    
        return res