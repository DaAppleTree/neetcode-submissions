class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen = set()
            for c in range(9):
                if board[r][c] in seen:
                    return False
                if board[r][c] != ".":
                    seen.add(board[r][c])

        for c in range(9):
            seen = set()
            for r in range(9):
                if board[r][c] in seen:
                    return False
                if board[r][c] != ".":
                    seen.add(board[r][c])

        for R in range(3):
            for C in range(3):
                seen = set()
                for r in range(3*R, 3*R+3):
                    for c in range(3*C, 3*C+3):
                        if board[r][c] in seen:
                            return False
                        if board[r][c] != ".":
                            seen.add(board[r][c])

        return True
        