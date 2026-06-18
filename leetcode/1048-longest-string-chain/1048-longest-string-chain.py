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
        dp = [1] * (n + 1)

        for i in range(n):
            for prev in range(i):
                small, longer = words[prev], words[i]
                if compare(small, longer):
                    dp[i] = max(dp[i], dp[prev] + 1)
        return max(dp)
# [1, 1, 2, 3, 3, 4]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna