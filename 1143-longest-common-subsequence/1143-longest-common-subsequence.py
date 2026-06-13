class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[float('-inf')] * m for _ in range(n)]

        def common(i, j):

            if i < 0 or j < 0:
                return 0
            if dp[i][j] != float('-inf'):
                return dp[i][j]

            matches, nomatches = float('-inf'), float('-inf')
            if text1[i] == text2[j]:
                matches = 1 + common(i - 1, j - 1)
            else:
                nomatches = 0 + max(common(i - 1, j), common(i, j - 1))
            val = max(matches, nomatches)
            dp[i][j] = val
            return val

        return common(n - 1, m - 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna