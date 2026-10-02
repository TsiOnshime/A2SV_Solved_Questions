class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        state = [['.'] * n for _ in range(n)]

        def is_valid(c, r):
            # same row
            for cc in range(c):
                if state[r][cc] == "Q":
                    return False
            
            # upper-left diagonal
            rr, cc = r - 1, c - 1
            while rr >= 0 and cc >= 0:
                if state[rr][cc] == "Q":
                    return False
                rr -= 1
                cc -= 1
            
            # lower-left diagonal 
            rr, cc = r + 1, c - 1
            while rr < n and cc >= 0:
                if state[rr][cc] == "Q":
                    return False
                rr += 1
                cc -= 1

            return True

        def solve(c):
            nonlocal state
            if c == n:
                res.append(["".join(row) for row in state])
                return 
            
            for r in range(n):
                if is_valid(c, r):
                    state[r][c] = "Q"
                    solve(c + 1)
                    state[r][c] = "."
        solve(0)
        return res



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna