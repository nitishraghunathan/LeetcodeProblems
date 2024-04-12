class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for i in range(len(board))] 
        columns = [set() for i in range(len(board))]
        box= [set() for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    columns[j].add(board[i][j])
                    box[(i//3)*3 + j//3].add(board[i][j])
        def backtracking(row, col):
            nonlocal solved
            if len(board) == row:
                solved = True
                return
            new_row = row + (col+1)//9
            new_col = (col+1)%9
            if board[row][col] != '.':
                backtracking(new_row, new_col)
                return
            box_id = (row//3)*3 + col//3
            for i in range(1,10):
                i=str(i)
                if i not in columns[col] and i not in rows[row] and i not in box[box_id]:
                    rows[row].add(i)
                    columns[col].add(i)
                    box[box_id].add(i)
                    board[row][col] = i
                    backtracking(new_row, new_col)
                    if not solved:
                        rows[row].remove(i)
                        columns[col].remove(i)
                        box[box_id].remove(i)
                        board[row][col] = '.'

        solved = False
        backtracking(0,0)
        return board
