class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, x, y, index, word):
            if index == len(word):
                return True 
            if x < 0 or y < 0 or x > len(board)-1 or y > len(board[x])-1 or board[x][y] != word[index]:
                return False
            temp = board[x][y]
            board[x][y] = '#'
            value =  dfs(board, x+1, y, index+1, word) or dfs(board,x-1, y, index+1, word) or dfs(board, x, y+1, index+1, word) or dfs(board, x, y-1, index+1, word)
            board[x][y] = temp
            return value
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if dfs(board, i, j, 0, word):
                        return True
        return False
