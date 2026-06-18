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
        dp = [[-1] * (n + 1) for _ in range(n)]

        def calcLength(i, prev_index):
            if i == n:
                return 0
            if dp[i][prev_index + 1] != -1:
                return dp[i][prev_index + 1]

            take = 0
            small = words[prev_index]
            longer = words[i]

            if prev_index == -1:
                take = 1 + calcLength(i + 1, i)
            else:
                truth = compare(small, longer) 
                if truth:
                    take = 1 + calcLength(i + 1, i)
            notake = calcLength(i + 1, prev_index)
            val = max(take, notake)
            dp[i][prev_index + 1] = val
            return val

        return calcLength(0, -1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna