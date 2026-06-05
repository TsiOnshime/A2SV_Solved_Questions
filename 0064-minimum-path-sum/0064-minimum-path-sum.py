class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [0] * n
    #l = 8 , u = 6
        # [6, 8, 7]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i] = grid[i][j]
                else:
                    left = float('inf')
                    up = float('inf')

                    if j - 1 >= 0:
                        left = dp[j - 1]
                    if i - 1 >= 0:
                        up = dp[j]
                    val = min(left, up)
                    dp[j] = val + grid[i][j]

        return dp[-1]



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna