class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        

        n, m = len(s), len(t)
        prev = [0] * (m + 1)
        curr = [0] * (m + 1)
        curr[0] = 1
        prev[0] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    curr[j] = prev[j - 1] + prev[j]
                else:
                    curr[j] = prev[j]

            prev = curr.copy()

        return prev[m]

      

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna