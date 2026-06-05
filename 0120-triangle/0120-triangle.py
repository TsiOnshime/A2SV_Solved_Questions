class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows, cols = len(triangle), len(triangle[-1])

        dp = [[-1] * cols for i in range(rows)]

        for i in range(cols):
            dp[-1][i] = triangle[-1][i]

        for i in range(rows - 2, -1, -1):
            for j in range(i, -1, -1):
                down = dp[i + 1][j]
                diagonal = dp[i + 1][j + 1]
                val = min(down, diagonal)
                dp[i][j] = val + triangle[i][j]

        return dp[0][0]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna