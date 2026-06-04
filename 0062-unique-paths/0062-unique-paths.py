class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for i in range(m)]
        print(dp)
        def paths(i, j):

            if i >= m or j >= n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]

            val = paths(i + 1, j) + paths(i, j + 1)
            dp[i][j] = val
            return val



        return paths(0, 0)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna