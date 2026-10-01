class Solution:
    def isValidSudoku(self, board):
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        s = [set() for _ in range(9)] 

        for r in range(9):
            for c in range(9):
                si = (r//3) + (c//3 *3)
                if board[r][c] == ".":
                    continue
                if board[r][c] in row[r] or board[r][c] in col[c]  or board[r][c] in s[si]:
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                s[si].add(board[r][c])
        return True

            
                