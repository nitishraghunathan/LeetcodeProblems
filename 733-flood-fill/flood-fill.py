class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def flood(x, y, color, curr):
            if x < 0 or  y < 0 or x > len(image) -1 or y >len(image[x])-1 or image[x][y] == color or image[x][y] != curr:
                return
            image[x][y] = color 
            flood(x+1,y, color, curr)
            flood(x-1,y, color, curr)
            flood(x, y+1, color, curr)
            flood(x, y-1, color, curr)
            return
        flood(sr, sc, color, image[sr][sc])
        return image  
        