class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # top down
        rows, cols = len(matrix), len(matrix[0])
        _min = float('inf')
        dp = [[float('inf')]* cols for r in range(rows)]
        def pathSum(i, j):
            if j < 0 or j >= cols:
                return float('inf')
            if i == rows - 1:
                return matrix[i][j]
            if dp[i][j] != float('inf'):
                return dp[i][j]
            down = matrix[i][j] + pathSum(i + 1, j)
            downleft = matrix[i][j] + pathSum(i + 1, j - 1)
            downright = matrix[i][j] + pathSum(i + 1, j + 1)

            val = min(down, downleft, downright)

            dp[i][j] = val

            return val

        for i in range(cols):
            _min = min(_min, pathSum(0, i))

        return _min

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna