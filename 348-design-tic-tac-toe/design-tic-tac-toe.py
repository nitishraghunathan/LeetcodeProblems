class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0]*n
        self.cols = [0]*n
        self.negative_diagnol = 0
        self.positive_diagnol = 0
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        move = 1 if player == 1 else -1
        self.rows[row] += move
        self.cols[col] += move 
        if row==col:
            self.negative_diagnol += move 
        if row+col ==self.n-1:
            self.positive_diagnol += move 
        if self.rows[row] == self.n or self.cols[col]==self.n or self.positive_diagnol == self.n or self.negative_diagnol == self.n:
            return 1
        if self.rows[row] == -self.n or self.cols[col]==-self.n or self.positive_diagnol == -self.n or self.negative_diagnol == -self.n:
            return 2
        return 0
        


        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)