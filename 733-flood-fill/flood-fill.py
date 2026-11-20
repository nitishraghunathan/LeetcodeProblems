class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        def dfs(i,j,color, fill):
            if i < 0 or j < 0 or i > len(image)-1 or j > len(image[i])-1 or image[i][j] != fill or image[i][j]==color:
                return
            image[i][j] = color
            dfs(i+1,j,color, fill)
            dfs(i-1,j,color, fill)
            dfs(i,j+1,color, fill)
            dfs(i,j-1,color, fill)
            return
        dfs(sr,sc, color, image[sr][sc])
        return image
        