class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = [1] * n
# [1, 1, 1]
        for i in range(1, m):
            for j in range(1, n):
                rows[j] = rows[j] + rows[j - 1]
        
        return rows[-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna