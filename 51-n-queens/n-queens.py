class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        columns = set()
        positive_diagnol = set()
        negative_diagnol = set()
        result = []
        def backtracking(row):
            nonlocal result
            if row == n:
                result.append([''.join(r) for r in board])
                return result
            for c in range(n):
                if c in columns or row+c in positive_diagnol or row-c in negative_diagnol:
                    continue
                else:
                    board[row][c] = 'Q'
                    columns.add(c)
                    positive_diagnol.add(row+c)
                    negative_diagnol.add(row-c) 
                    result = backtracking(row+1)
                    board[row][c] = '.'
                    negative_diagnol.remove(row-c) 
                    positive_diagnol.remove(row+c) 
                    columns.remove(c)
            return result
        board = [['.']*n for i in range(n)]
        return backtracking(0)