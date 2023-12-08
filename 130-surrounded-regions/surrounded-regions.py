class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Conditions 

        1. Convert all 'O' 4 directionally surrounded by 'X'
        2. Do not Flip 'O's on the border or 'O's that are adjacent to those that 
        re not flipped

        3. Flip Os that are on the border or adjacent to these no flipped Os to a different alphabet
        4. We will do a second pass in flipping 'O's to  'X's and the remaining back to 'O's
        """

        def dfs(board,i,j):
            if i <0 or j <0 or i > len(board) - 1 or j > len(board[0])-1 or board[i][j]=='X' or board[i][j]=='W':
                return
            board[i][j]='W'
            dfs(board, i+1,j)
            dfs(board, i-1,j)
            dfs(board, i,j+1)
            dfs(board, i,j-1)
            return

        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or j==0 or i == len(board)-1 or j == len(board[0])-1:
                    dfs(board, i, j)
    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'W':
                    board[i][j]='O'
                else:
                    board[i][j]='X'
        return board
