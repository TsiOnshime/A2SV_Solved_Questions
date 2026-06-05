class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[float('inf')]*cols for r in range(rows)]

        for i in range(cols):
            dp[rows - 1][i] = matrix[rows - 1][i]


        for i in range(rows - 2, -1, -1):
            for j in range(cols):
                down = dp[i + 1][j]
                downleft = float('inf')
                downright = float('inf')

                if j - 1 >= 0:
                    downleft = dp[i + 1][j - 1]
                if j + 1 < cols:
                    downright = dp[i + 1][j + 1]

                val = min(down, downleft, downright)

                dp[i][j] = val + matrix[i][j]

        return min(dp[0])

                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna