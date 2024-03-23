class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        columns = set()
        positive_diagnols = set() 
        negative_diagnols = set() 
        board = [['.']*n for i in range(n)]
        def backtracking(row:int, n:int, columns:set, positive_diagnols:set, negative_diagnols:set, board:list, result:list):
            if row == n:
                new_list = [''.join(r) for r in board]
                result.append(list(new_list))
                return result
            for c in range(n):
                if c in columns or row+c in positive_diagnols or row-c in negative_diagnols:
                    continue 
                columns.add(c)
                positive_diagnols.add(row+c)
                negative_diagnols.add(row-c)
                board[row][c] = 'Q'
                result=backtracking(row+1, n, columns, positive_diagnols, negative_diagnols, board, result)
                board[row][c] = '.'
                positive_diagnols.remove(row+c) 
                negative_diagnols.remove(row-c)
                columns.remove(c)
            return result
        return backtracking(0, n, columns, positive_diagnols, negative_diagnols, board, [])

                


        