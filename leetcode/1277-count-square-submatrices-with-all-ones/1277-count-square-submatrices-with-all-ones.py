class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * m for _ in range(n)]

        squares = 0
        for j in range(m):
            dp[0][j] = matrix[0][j]
            squares += dp[0][j]

        for i in range(1, n):
            dp[i][0] = matrix[i][0]
            squares += dp[i][0]

        for i in range(1, n):
            for j in range(1, m):
                top = dp[i - 1][j]
                left = dp[i][j - 1]
                diagonal = dp[i - 1][j - 1]
                if matrix[i][j] == 1:
                    dp[i][j] = 1 + min(top, left, diagonal)
                
                squares += dp[i][j]
        return squares

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna