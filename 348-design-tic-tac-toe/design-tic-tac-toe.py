class TicTacToe:

    def __init__(self, n: int):
        self.grid = [['.']*n for i in range(n)]
        

    def move(self, row: int, col: int, player: int) -> int:
        def check_winner(player, row, col):
            move = 'X' if player==1 else 'O'
            self.grid[row][col] = move
            flag_one = True
            flag_two = True
            flag_diag_one = True
            flag_diag_two = True
            for i in range(len(self.grid)):
                if self.grid[row][i] != move:
                    flag_one = False
                if self.grid[i][col] !=move:
                    flag_two = False
                if self.grid[i][i] != move:
                    flag_diag_one = False
                if self.grid[i][len(self.grid)-1-i] !=move:
                    flag_diag_two= False

            return flag_diag_one or flag_diag_two or flag_one or flag_two
        return player if check_winner(player, row, col) else 0

        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)