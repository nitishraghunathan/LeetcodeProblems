class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def dfs(i, j, board):
            if i < 0 or i > len(board)-1 or j < 0 or j > len(board[i])-1 or board[i][j]== '.':
                return
            board[i][j] = '.'
            dfs(i+1,j, board)
            dfs(i-1,j, board)
            dfs(i,j+1, board)
            dfs(i,j-1, board)
        count = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X':
                    dfs(i,j, board)
                    count +=1
        return count
