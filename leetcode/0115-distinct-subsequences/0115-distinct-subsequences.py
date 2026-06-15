class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        

        n, m = len(s), len(t)

        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1
        for j in range(1, m + 1):
            dp[0][j] = 0
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][m]

      

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna