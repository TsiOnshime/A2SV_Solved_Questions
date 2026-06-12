class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

        def subsequence(i, j):
            if i == 0 or j == 0:
                return 0
            if dp[i][j] != float('-inf'):
                return dp[i][j]

            matched = float('-inf')
            notmatched = float('-inf')
            if text1[i - 1] == text2[j - 1]:
                matched = 1 + subsequence(i - 1, j - 1)
            else:
                notmatched = max(subsequence(i - 1, j), subsequence(i, j - 1))

            val = max(matched, notmatched)
            dp[i][j] = val

            return val

        return subsequence(n, m)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna