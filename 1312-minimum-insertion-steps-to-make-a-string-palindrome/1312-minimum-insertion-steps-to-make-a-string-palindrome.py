class Solution:
    def minInsertions(self, s: str) -> int:
        palindrome = 0

        n = len(s)
        t = s[::-1]

        dp = [[float('-inf')] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[0][i] = 0
            dp[i][0] = 0
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                palindrome = max(palindrome, dp[i][j])
        
        return len(s) - palindrome




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna