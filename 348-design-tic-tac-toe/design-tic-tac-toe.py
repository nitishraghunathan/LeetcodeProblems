class TicTacToe:
    def __init__(self, n: int):
        ## RC ##
        ## APPROACH : GREEDY ##
        ## Similar to leetcode: 36. Valid Sudoku ##
        
		## TIME COMPLEXITY : O(1) ##
		## SPACE COMPLEXITY : O(N) ##

        self.rows = [0] * n         # store total sums by row
        self.cols = [0] * n         # store total sums by column
        self.diagonal = 0           # store total sums by diagonal i.e (row == col)
        self.anti_diagonal = 0      # store total sums by anti-diagonal i.e (row == n-col-1)
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        value = 1 if(player == 1) else -1
        
        self.rows[row] += value
        self.cols[col] += value
        
        if(row == col):
            self.diagonal += value
        if(row == (self.n - 1) - col):                  # Anti diagonal
            self.anti_diagonal += value
                    
        if(self.rows[row] == -self.n or self.cols[col] == -self.n or self.anti_diagonal == -self.n or self.diagonal == -self.n):
            return 2
        
        if(self.rows[row] == self.n or self.cols[col] == self.n or self.anti_diagonal == self.n or self.diagonal == self.n):
            return 1
        
        return 0