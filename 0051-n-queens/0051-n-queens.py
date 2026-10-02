class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        state = [['.'] * n for _ in range(n)]

        upper_left = defaultdict(bool)
        lower_left = defaultdict(bool)
        row = defaultdict(bool)

        def is_valid(c, r):
            if row[r] == True:
                return False
            
            if upper_left[c - r] == True:
                return False
            
            if lower_left[c + r] == True:
                return False
            
            return True

        def solve(c):
            if c == n:
                res.append(["".join(row) for row in state])
                return 
            
            for r in range(n):
                if is_valid(c, r):
                    row[r] = True
                    upper_left[c - r] = True
                    lower_left[c + r] = True 
                    state[r][c] = "Q"
                    solve(c + 1)
                    state[r][c] = "."
                    row[r] = False
                    upper_left[c - r] = False
                    lower_left[c + r] = False
        solve(0)
        return res



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna