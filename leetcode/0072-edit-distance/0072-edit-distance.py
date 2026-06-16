class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float('inf')] * len(word2) for _ in range(len(word1))]

        def findMinDistance(i, j):
            if j < 0:
                return i + 1
            if i < 0:
                return j + 1
            if dp[i][j] != float('inf'):
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = findMinDistance(i - 1, j - 1)
            else:
                # insert
                ins = 1 + findMinDistance(i, j - 1)
                # delete
                dele = 1 + findMinDistance(i - 1, j)
                # replace
                rep = 1 + findMinDistance(i - 1, j - 1)

                dp[i][j] = min(ins, dele, rep)
            return dp[i][j]

        return findMinDistance(len(word1) - 1, len(word2) - 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna