class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [["."] * n for _ in range(n)]
        res = []
        def isSafe(col, row):
            r, c = row, col
            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                c -= 1
                r -= 1
            r, c = row, col
            while c >= 0:
                if board[r][c] == "Q":
                    return False
                c -= 1
            r, c = row, col
            while r < n and c >= 0:
                if board[r][c] == "Q":
                    return False
                c -= 1
                r += 1
            return True

        def solve(col):
            if col == n:
                res.append(["".join(row) for row in board])
                return 
            

            for row in range(n):
                if isSafe(col, row):
                    board[row][col] = "Q"
                    solve(col + 1)
                    board[row][col] = "."

        solve(0)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna