class Solution:
    def isValidSudoku(self, board):
        r = [set() for _ in range(9)]
        c = [set() for _ in range(9)]
        s = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9): 
            row  = i
            sqr = math.floor(row/3)
            for j in range(9):
                col  = j
                sqc = math.floor(col/3)
                if(board[row][col] == "."):
                    continue
                if board[row][col] in r[row] or board[row][col] in c[col]:
                    return False

                if board[row][col] in s[sqr][sqc]:
                    return False
                r[row].add(board[row][col])
                c[col].add(board[row][col])
                s[sqr][sqc].add(board[row][col])
        return True