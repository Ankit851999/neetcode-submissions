class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        clo = [ set() for _ in range(9)]
        row = [ set() for _ in range(9)]
        box = [ [set() for _ in range(3)]for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif (
                    board[i][j] in clo[j]
                 or board[i][j] in row[i] 
                 or board[i][j] in box[i//3][j//3]
                 ):
                    return False
                else:
                    clo[j].add(board[i][j])
                    row[i] .add(board[i][j])
                    box[i//3][j//3].add(board[i][j])
        return True