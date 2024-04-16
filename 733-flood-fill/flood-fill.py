class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(image, i, j, color, paint):
            if i < 0 or j < 0 or i > len(image)-1 or j > len(image[i])-1 or image[i][j]==color or image[i][j] != paint:
                return
            image[i][j] = color 
            dfs(image, i+1,j,color, paint)
            dfs(image, i-1,j,color, paint)
            dfs(image, i,j-1,color, paint)
            dfs(image, i,j+1,color, paint)
        dfs(image, sr, sc, color, image[sr][sc])
        return image