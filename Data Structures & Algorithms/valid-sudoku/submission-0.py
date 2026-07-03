class Solution:
    def isValidSudoku(self, board):
        r = [{} for _ in range(9)]
        c = [{} for _ in range(9)]
        s = [[{} for _ in range(3)] for _ in range(3)]
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
                else:
                    r[row][board[row][col]] =  True
                    c[col][board[row][col]] = True
                if board[row][col] in s[sqr][sqc]:
                    return False
                else:
                    s[sqr][sqc][board[row][col]] = True
        return True