class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        words.sort(key = len)
        def compare(small, longer):
            if len(longer) != len(small) + 1: return False
            i = j = 0

            while i < len(longer):
                if j < len(small) and longer[i] == small[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            return i == len(longer) and j == len(small)
        n = len(words)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for prev in range(-1, i):
                small, longer = words[prev], words[i]
                take = 0
                if prev == -1:
                    take = 1 + dp[i + 1][i + 1]
                else:
                    if compare(small, longer):
                        take = 1 + dp[i + 1][i + 1]
                notake = dp[i + 1][prev + 1]
                val = max(take, notake)
                dp[i][prev + 1] = val
        return dp[0][0]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna