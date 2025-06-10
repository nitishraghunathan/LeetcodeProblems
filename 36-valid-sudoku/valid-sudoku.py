class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box = [set() for i in range(9)]
        column = [set() for j in range(9)]
        row = [set() for k in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    if board[i][j] in column[j]:
                        return False
                    if board[i][j] in row[i]:
                        return False
                    id = (i//3)*3 + j//3
                    if board[i][j] in box[id]:
                        return False
                    row[i].add(board[i][j])
                    column[j].add(board[i][j])
                    box[id].add(board[i][j])
        return True
        