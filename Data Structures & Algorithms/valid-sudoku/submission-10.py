class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [0] * 9
        clo = [0] * 9
        box = [0] * 9
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                val = int(board[i][j])-1
                if (
                    (1 << val) & row[i] or
                    (1 << val) & clo[j] or
                    (1 << val) & box[(i//3)*3 + (j//3)]
                    ):
                    return False
                row[i] |= (1 << val)
                clo[j] |= (1 << val)
                box[(i//3)*3 + (j//3)] |= (1 << val)
        return True