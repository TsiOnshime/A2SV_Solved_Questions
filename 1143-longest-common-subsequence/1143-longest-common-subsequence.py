class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0
        for j in range(m + 1):
            dp[0][j] = 0
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                matches, nomatches = float('-inf'), float('-inf')
                if text1[i - 1] == text2[j - 1]:
                    matches = 1 + dp[i - 1][j - 1]
                else:
                    nomatches = 0 + max(dp[i - 1][j], dp[i][j - 1])
                val = max(matches, nomatches)
                dp[i][j] = val         
        return dp[n][m]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna