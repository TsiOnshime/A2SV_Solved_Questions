class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        max_side = 0
        dp = [[0] * cols for r in range(rows)]
       
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "0":
                    continue
                _min = float('inf')
                _min = min(_min, int(dp[r - 1][c]) if r - 1 >= 0 else 0)
                _min = min(_min, int(dp[r][c - 1]) if c - 1 >= 0 else 0)
                _min= min(_min, int(dp[r - 1][c - 1]) if r - 1 >= 0 and c - 1 >= 0 else 0)
        
                dp[r][c] = _min + 1
                max_side = max(max_side, dp[r][c])
    
        return max_side * max_side




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna