class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrack(i,j):
            nonlocal solved
            if i == len(board):
                solved = True
                return 
            new_i = i + (j+1)//9
            new_j = (j+1)%9
            if board[i][j] != '.':
                backtrack(new_i, new_j)
            else:
                for k in range(1, 10):
                    k =str(k)
                    if k not in rows[i] and k not in boxes[(i//3)*3 + j//3] and k not in cols[j]:
                        cols[j].add(k)
                        rows[i].add(k)
                        boxes[(i//3)*3 + j//3].add(k)
                        board[i][j] = k
                        backtrack(new_i, new_j)
                        if not solved:
                            cols[j].remove(k)
                            rows[i].remove(k)
                            boxes[(i//3)*3 + j//3].remove(k)
                            board[i][j] ='.'

        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] !='.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[(i//3) * 3 + j//3].add(board[i][j])
        solved = False
        backtrack(0,0)
        return board