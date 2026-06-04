class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def path(i, j):
            if i >= m or j >= n:
                return float('inf')
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            down = grid[i][j] + path(i + 1, j)
            right = grid[i][j] + path(i, j + 1)
            val = min(down, right)
            dp[i][j] = val

            return val

        dp = [[-1] * n for i in range(m)]
        return path(0, 0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna