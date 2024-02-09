class Solution:
    def tictactoe(self, move: List[List[int]]) -> str:
        grid = [[1,2,3],[4,5,6],[7,8,9]]
        def check_winner(moves, i, j):
            if moves[i][0] == moves[i][1] == moves[i][2]:
                return True
            if moves[0][j] == moves[1][j] == moves[2][j]:
                return True
            if moves[0][0] == moves[1][1] == moves[2][2]:
                return True
            if moves[0][2] == moves[1][1] == moves[2][0]:
                return True
            return False
        for i in range(len(move)):
            winner = 'A' if i%2==0 else 'B'
            grid[move[i][0]][move[i][1]] = 'X'  if i%2==0 else 'O'
            iswinner = check_winner(grid, move[i][0] ,move[i][1])
            if iswinner:
                return winner
        return 'Draw' if len(move) == 9 else 'Pending'
