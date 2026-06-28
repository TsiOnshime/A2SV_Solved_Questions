class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [["."] * n for _ in range(n)]
        res = []
        leftRow = [0] * n
        lowerDiagonal = [0] * (2 * n - 1)
        upperDiagonal = [0] * (2 * n - 1)
        def isSafe(col, row):
            nonlocal leftRow
            nonlocal lowerDiagonal
            nonlocal upperDiagonal

            if leftRow[row] != 0:
                return False
            if lowerDiagonal[col + row] != 0:
                return False
            if upperDiagonal[n - 1 + col - row] != 0:
                return False
            
            return True

        def solve(col):
            if col == n:
                res.append(["".join(row) for row in board])
                return 
            

            for row in range(n):
                if isSafe(col, row):
                    leftRow[row] = 1
                    lowerDiagonal[col + row] = 1
                    upperDiagonal[n - 1 + col - row] = 1
                    board[row][col] = "Q"
                    solve(col + 1)
                    leftRow[row] = 0
                    lowerDiagonal[col + row] = 0
                    upperDiagonal[n - 1 + col - row] = 0
                    board[row][col] = "."

        solve(0)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna